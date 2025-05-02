import os
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Import data from the corresponding Python files
from data.ratings import user_ratings  # Assuming user_ratings is a list or pandas DataFrame
from data.movies import movies         # Assuming movies is a list or pandas DataFrame
from data.books import books           # Assuming books is a list or pandas DataFrame

def build_utility_matrix(ratings, items):
    """
    Builds a utility matrix where rows are user IDs and columns are item IDs.
    Missing ratings are filled with 0.
    """
    # Convert user_ratings into a DataFrame if it's a list or dictionary
    ratings_df = pd.DataFrame(ratings)
    
    # Build the utility matrix: users as rows and items as columns
    utility = ratings_df.pivot_table(index='user_id', columns='item_id', values='rating', fill_value=0)
    return utility

def recommend_items(user_id, utility_matrix, items, top_n=5):
    """
    Recommends items for a given user based on collaborative filtering.
    Returns at least 5 items, and if fewer than 5, returns all available recommendations.
    """
    if user_id not in utility_matrix.index:
        return []

    user_vector = utility_matrix.loc[user_id].values.reshape(1, -1)
    similarity = cosine_similarity(user_vector, utility_matrix)[0]

    similar_users = pd.Series(similarity, index=utility_matrix.index)
    similar_users = similar_users.drop(user_id).sort_values(ascending=False)

    scores = pd.Series(dtype=float)

    for other_user_id, sim_score in similar_users.items():
        other_user_ratings = utility_matrix.loc[other_user_id]
        for item_id in utility_matrix.columns:
            if utility_matrix.at[user_id, item_id] == 0 and other_user_ratings[item_id] > 0:
                if item_id not in scores:
                    scores[item_id] = 0.0  # Explicitly cast to float
                scores[item_id] += sim_score * other_user_ratings[item_id]

    if scores.empty:
        return []

    # Ensure all scores are explicitly cast to float to avoid dtype issues
    scores = scores.astype(float)

    # Sort by score and get top N item IDs
    recommended_item_ids = scores.sort_values(ascending=False).head(top_n).index.tolist()

    # If there are fewer than 'top_n' recommendations, include all available recommendations
    if len(recommended_item_ids) < top_n:
        recommended_item_ids = scores.sort_values(ascending=False).index.tolist()

    # Map item IDs to titles (using the loaded items)
    item_map = {item['item_id']: item['title'] for item in items}
    recommendations = [item_map[item_id] for item_id in recommended_item_ids if item_id in item_map]

    return recommendations

# Example usage
def main():
    # Example: Get recommendations for a user using movies
    user_id = 2  # Replace with an actual user ID
    
    # Build the utility matrix using the movie data
    utility_matrix = build_utility_matrix(user_ratings, movies)
    recommendations = recommend_items(user_id, utility_matrix, movies)

    print(f"Recommendations for User {user_id}:")
    for rec in recommendations:
        print(f"- {rec}")

if __name__ == "__main__":
    main()
