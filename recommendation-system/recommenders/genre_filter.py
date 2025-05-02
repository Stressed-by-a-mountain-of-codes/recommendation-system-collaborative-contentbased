def filter_by_genre(items, genre, item_type="movie"):
    """
    Filters movies/books by genre.

    Parameters:
    - items: List of movies or books (as dictionaries).
    - genre: Genre to filter by (string).
    - item_type: "movie" or "book". Determines the item type for filtering.

    Returns:
    - Filtered list of items by genre.
    """
    filtered_items = []
    print(f"[DEBUG] Filtering {item_type}s by genre: '{genre}'...")  # Debugging statement

    # Check if the items are movies or books and filter based on genre
    for item in items:
        if item_type == "movie" and 'genre' in item and genre.lower() in item['genre'].lower():
            filtered_items.append(item)
        elif item_type == "book" and 'genre' in item and genre.lower() in item['genre'].lower():
            filtered_items.append(item)

    # Debugging output based on filtered results
    if not filtered_items:
        print(f"[DEBUG] No {item_type}s found with the genre '{genre}'.")  # Debugging statement
    else:
        print(f"[DEBUG] Found {len(filtered_items)} {item_type}s with the genre '{genre}'.")  # Debugging statement

    return filtered_items


def filter_movies_by_genre(genre):
    """
    Wrapper for filtering movies by genre.
    """
    print(f"[DEBUG] Filtering movies by genre '{genre}'...")  # Debugging statement
    return filter_by_genre(movies, genre, item_type="movie")


def filter_books_by_genre(genre):
    """
    Wrapper for filtering books by genre.
    """
    print(f"[DEBUG] Filtering books by genre '{genre}'...")  # Debugging statement
    return filter_by_genre(books, genre, item_type="book")


if __name__ == "__main__":
    # Example debugging calls
    genre = input("Enter the genre you want to filter by: ").strip()

    # Ask user for the type of items to filter: Movies or Books
    print("Choose Item Type to Filter:")
    print("1. Movies")
    print("2. Books")
    item_choice = input("Enter 1 or 2: ").strip()

    if item_choice == "1":
        filtered_movies = filter_movies_by_genre(genre)
        print(f"\nFiltered Movies by genre '{genre}':")
        for movie in filtered_movies:
            print(f"- {movie['title']}")

    elif item_choice == "2":
        filtered_books = filter_books_by_genre(genre)
        print(f"\nFiltered Books by genre '{genre}':")
        for book in filtered_books:
            print(f"- {book['title']}")

    else:
        print("Invalid choice. Please select 1 for Movies or 2 for Books.")
