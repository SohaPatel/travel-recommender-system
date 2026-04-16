from src.recommenders.content_based import recommend_by_preferences
from src.recommenders.collaborative import recommend_for_user_userbased
from src.recommenders.hybrid import hybrid_merge_and_rank

import pandas as pd
from flask import Flask, request, jsonify

# Load datasets
places_df = pd.read_csv("data/processed/places_clean_with_id.csv")
df_features = pd.read_csv("data/processed/places_features.csv")
ratings_df = pd.read_csv("data/simulated/user_ratings.csv")

app = Flask(__name__)

def people_to_crowd_level(n: int) -> str:
    if n <= 2:
        return "low"
    if n <= 5:
        return "medium"
    return "high"


@app.get("/api/health")
def health():
    return jsonify({"status": "ok"})


@app.post("/api/recommend/manual")
def recommend_manual():

    data = request.get_json(force=True)

    interest = data.get("interest", "")
    place_category = data.get("place_category", "")
    season = data.get("best_season_to_visit", "")
    people = int(data.get("people", 2))
    top_n = int(data.get("top_n", 10))

    crowd_level = people_to_crowd_level(people)

    results = recommend_by_preferences(
        df_features,
        top_n=top_n,
        place_category=place_category,
        interest=interest,
        crowd_level=crowd_level,
        best_season_to_visit=season
    )

    return jsonify(results.to_dict(orient="records"))


@app.post("/api/recommend/collaborative")
def recommend_collaborative():

    data = request.get_json(force=True)

    user_id = data.get("user_id", "U1")
    top_n = int(data.get("top_n", 10))

    results = recommend_for_user_userbased(
        ratings_df=ratings_df,
        places_df=places_df,
        target_user_id=user_id,
        top_n=top_n,
        k_neighbors=15
    )

    return jsonify(results.to_dict(orient="records"))


@app.post("/api/recommend/hybrid")
def recommend_hybrid():

    data = request.get_json(force=True)

    interest = data.get("interest", "")
    place_category = data.get("place_category", "")
    season = data.get("best_season_to_visit", "")
    people = int(data.get("people", 2))

    top_n = int(data.get("top_n", 10))
    alpha = float(data.get("alpha", 0.6))

    user_id = data.get("user_id", "U1")

    crowd_level = people_to_crowd_level(people)

    content_recs = recommend_by_preferences(
        df_features,
        top_n=50,
        place_category=place_category,
        interest=interest,
        crowd_level=crowd_level,
        best_season_to_visit=season
    )

    if "item_id" not in content_recs.columns:
        join_cols = [
            c for c in ["popular_destination", "city", "state"]
            if c in content_recs.columns and c in places_df.columns
        ]

        if join_cols:
            content_recs = content_recs.merge(
                places_df[["item_id"] + join_cols],
                on=join_cols,
                how="left"
            )

    cf_recs = recommend_for_user_userbased(
        ratings_df=ratings_df,
        places_df=places_df,
        target_user_id=user_id,
        top_n=50,
        k_neighbors=15
    )

    hybrid = hybrid_merge_and_rank(
        content_df=content_recs,
        cf_df=cf_recs,
        alpha=alpha,
        top_n=top_n
    )

    return jsonify(hybrid.to_dict(orient="records"))