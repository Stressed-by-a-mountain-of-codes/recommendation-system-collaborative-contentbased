# main.py

import os
from recommenders.genre_filter import filter_by_genre
from data.users import users

# Function to get the user's name by user ID
def get_user_name(user_id):
    user = next((u for u in users if u['user_id'] == user_id), None)
    return user['name'] if user else "Unknown"

def run_collaborative():
    from recommenders.collaborative import build_utility_matrix, recommend_items
    from data.ratings import user_ratings
    from data.movies import movies
    from data.books import books

    print("\nSelect Recommendation Type:")
    print("1. Movie")
    print("2. Book")
    choice = input("Enter your choice (1 or 2): ").strip()

    genre = input("Enter genre (leave empty for all genres): ").strip()

    user_id_input = input("Enter User ID: ").strip()
    try:
        user_id = int(user_id_input)
    except ValueError:
        print("Invalid User ID. Please enter a numeric value.")
        return

    user_name = get_user_name(user_id)
    print(f"Recommendations for {user_name}:")

    if choice == "1":
        utility = build_utility_matrix(user_ratings, movies)
        if user_id not in utility.index:
            print("No recommendations available for this user.")
            return
        recommendations = recommend_items(user_id, utility, movies)
        if genre:
            recommendations = [
                rec for rec in recommendations
                if any(m['title'] == rec and genre.lower() in m['genre'].lower() for m in movies)
            ]

    elif choice == "2":
        utility = build_utility_matrix(user_ratings, books)
        if user_id not in utility.index:
            print("No recommendations available for this user.")
            return
        recommendations = recommend_items(user_id, utility, books)
        if genre:
            recommendations = [
                rec for rec in recommendations
                if any(b['title'] == rec and genre.lower() in b['genre'].lower() for b in books)
            ]

    else:
        print("Invalid choice.")
        return

    if recommendations:
        for rec in recommendations:
            print(f"- {rec}")
    else:
        print("No recommendations found.")

def run_content_based():
    from recommenders.content_based import create_content_based_recommendations
    from data.movies import movies
    from data.books import books

    print("\nSelect Recommendation Type:")
    print("1. Movie")
    print("2. Book")
    choice = input("Enter your choice (1 or 2): ").strip()

    genre = input("Enter genre (leave empty for all genres): ").strip()

    filtered_movies = movies.copy()
    filtered_books = books.copy()

    if genre:
        if choice == "1":
            filtered_movies = filter_by_genre(filtered_movies, genre, item_type="movie")
        elif choice == "2":
            filtered_books = filter_by_genre(filtered_books, genre, item_type="book")
        else:
            print("Invalid choice.")
            return

    if choice == "1":
        recommendations = create_content_based_recommendations(filtered_movies, item_type="movie")
        for title, recs in recommendations.items():
            print(f"\n{title}:")
            print(f"- {', '.join(recs)}\n")
    elif choice == "2":
        recommendations = create_content_based_recommendations(filtered_books, item_type="book")
        for title, recs in recommendations.items():
            print(f"\n{title}:")
            print(f"- {', '.join(recs)}\n")
    else:
        print("Invalid choice.")

def run_gui():
    try:
        os.system("python gui_app.py")
    except Exception as e:
        print(f"[ERROR] Failed to launch GUI: {e}")

def main():
    while True:
        print("\n=== Recommendation System ===")
        print("1. Collaborative Filtering")
        print("2. Content-Based Filtering")
        print("3. Launch GUI")
        print("4. Exit")

        option = input("Enter your choice: ").strip()

        if option == "1":
            run_collaborative()
        elif option == "2":
            run_content_based()
        elif option == "3":
            run_gui()
        elif option == "4":
            print("Exiting the system.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
