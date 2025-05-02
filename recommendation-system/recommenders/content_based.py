# recommenders/content_based.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def create_content_based_recommendations(items, item_type="movie"):
    # Extract titles and genres
    titles = [item['title'] for item in items]
    genres = [item['genre'] for item in items]

    # Vectorize genres using TF-IDF
    tfidf = TfidfVectorizer(stop_words='english')
    genre_matrix = tfidf.fit_transform(genres)

    # Compute cosine similarity
    cosine_sim = linear_kernel(genre_matrix, genre_matrix)

    # Map item indices to titles
    title_indices = {title: idx for idx, title in enumerate(titles)}

    recommendations = {}
    for title in titles:
        idx = title_indices[title]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]  # Skip itself, get top 5
        similar_indices = [i[0] for i in sim_scores]
        similar_titles = [titles[i] for i in similar_indices]
        recommendations[title] = similar_titles

    return recommendations
