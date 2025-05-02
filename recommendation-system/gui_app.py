import tkinter as tk
from tkinter import messagebox
from recommenders.collaborative import recommend_items, build_utility_matrix
from recommenders.content_based import create_content_based_recommendations
from data.ratings import user_ratings
from data.movies import movies
from data.books import books
from data.users import users
from recommenders.genre_filter import filter_by_genre

# Function to get the user's name by user ID
def get_user_name(user_id):
    user = next((u for u in users if u['user_id'] == user_id), None)
    return user['name'] if user else "Unknown"

def run_collaborative(user_id, choice, genre):
    user_name = get_user_name(user_id)
    result_text.set(f"Recommendations for {user_name}:")

    recommendations = []  # Initialize to ensure it can be accessed safely.

    if choice == "1":  # Movie
        utility = build_utility_matrix(user_ratings, movies)
        if user_id not in utility.index:
            messagebox.showinfo("Error", "No recommendations available for this user.")
            return
        recommendations = recommend_items(user_id, utility, movies)
        if genre:
            recommendations = [
                rec for rec in recommendations
                if any(m['title'] == rec and genre.lower() in m['genre'].lower() for m in movies)
            ]
    elif choice == "2":  # Book
        utility = build_utility_matrix(user_ratings, books)
        if user_id not in utility.index:
            messagebox.showinfo("Error", "No recommendations available for this user.")
            return
        recommendations = recommend_items(user_id, utility, books)
        if genre:
            recommendations = [
                rec for rec in recommendations
                if any(b['title'] == rec and genre.lower() in b['genre'].lower() for b in books)
            ]

    if recommendations:
        display_recommendations(recommendations)
    else:
        result_text.set("No recommendations found.")

def run_content_based(user_id, choice, genre, actor, director):
    user_name = get_user_name(user_id)
    result_text.set(f"Recommendations for {user_name}:")

    recommendations = []  # Initialize to avoid UnboundLocalError

    if choice == "1":  # Movie
        filtered_movies = movies.copy()
        if genre:
            filtered_movies = filter_by_genre(filtered_movies, genre, item_type="movie")
        if actor:
            filtered_movies = [m for m in filtered_movies if any(a in m['actors'] for a in actor.split(','))]
        if director:
            filtered_movies = [m for m in filtered_movies if director.lower() in m['director'].lower()]
        recommendations = create_content_based_recommendations(filtered_movies, item_type="movie")
    elif choice == "2":  # Book
        filtered_books = books.copy()
        if genre:
            filtered_books = filter_by_genre(filtered_books, genre, item_type="book")
        if actor:
            filtered_books = [b for b in filtered_books if any(a in b['authors'] for a in actor.split(','))]
        if director:
            filtered_books = [b for b in filtered_books if director.lower() in b['authors']]
        recommendations = create_content_based_recommendations(filtered_books, item_type="book")

    if recommendations:
        display_recommendations(recommendations)
    else:
        result_text.set("No recommendations found.")

def display_recommendations(recommendations):
    rec_text = "\n".join([f"- {rec}" for rec in recommendations[:5]])  # Limit to top 5
    result_text.set(rec_text)

def on_submit():
    try:
        user_id = int(user_id_entry.get())  # Get user ID from input
        genre = genre_entry.get().strip()  # Get genre from input
        actor = actor_entry.get().strip()  # Get actor from input
        director = director_entry.get().strip()  # Get director from input
        choice = recommendation_choice.get()  # Get recommendation choice (Collaborative/Content-based)
        recommendation_type = movie_or_book_choice.get()  # Get recommendation type (Movie/Book)

        if choice == 1:  # Collaborative
            run_collaborative(user_id, recommendation_type, genre)
        elif choice == 2:  # Content-Based
            run_content_based(user_id, recommendation_type, genre, actor, director)
        else:
            messagebox.showinfo("Error", "Invalid recommendation choice.")
    except ValueError:
        messagebox.showinfo("Error", "Please enter a valid user ID.")

# GUI setup
root = tk.Tk()
root.title("Recommendation System")
root.geometry("600x600")  # Increased window size

# Title Label
tk.Label(root, text="Recommendation System", font=("Arial", 16)).grid(row=0, columnspan=2, pady=10)

# User ID
tk.Label(root, text="Enter User ID:").grid(row=1, column=0, sticky="e")
user_id_entry = tk.Entry(root)
user_id_entry.grid(row=1, column=1, padx=10)

# Recommendation Type (Collaborative or Content-Based)
tk.Label(root, text="Recommendation Type:").grid(row=2, column=0, sticky="e")
recommendation_choice = tk.IntVar()

# Collaborative Filtering option
tk.Radiobutton(root, text="Collaborative Filtering", variable=recommendation_choice, value=1).grid(row=2, column=1, sticky="w")

# Content-Based Filtering option
tk.Radiobutton(root, text="Content-Based Filtering", variable=recommendation_choice, value=2).grid(row=3, column=1, sticky="w")

# Movie or Book Filter (for Content-Based)
tk.Label(root, text="Choose Movie or Book:").grid(row=4, column=0, sticky="e")
movie_or_book_choice = tk.StringVar()
tk.Radiobutton(root, text="Movie", variable=movie_or_book_choice, value="1").grid(row=4, column=1, sticky="w")
tk.Radiobutton(root, text="Book", variable=movie_or_book_choice, value="2").grid(row=4, column=1, sticky="e")

# Genre Filter
tk.Label(root, text="Enter Genre (optional):").grid(row=5, column=0, sticky="e")
genre_entry = tk.Entry(root)
genre_entry.grid(row=5, column=1)

# Actor Filter (for Content-Based)
tk.Label(root, text="Enter Actor(s) (comma separated, optional):").grid(row=6, column=0, sticky="e")
actor_entry = tk.Entry(root)
actor_entry.grid(row=6, column=1)

# Director Filter (for Content-Based)
tk.Label(root, text="Enter Director (optional):").grid(row=7, column=0, sticky="e")
director_entry = tk.Entry(root)
director_entry.grid(row=7, column=1)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=8, columnspan=2, pady=10)

# Result Text (to display recommendations)
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left")
result_label.grid(row=9, columnspan=2, pady=10)

# Start the main loop
root.mainloop()
