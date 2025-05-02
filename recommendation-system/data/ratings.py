import pandas as pd

# Expanded user ratings for better collaborative filtering
data = [
    {"user_id": 1, "item_id": 101, "rating": 5},
    {"user_id": 1, "item_id": 102, "rating": 4},
    {"user_id": 1, "item_id": 103, "rating": 3},
    {"user_id": 1, "item_id": 104, "rating": 5},

    {"user_id": 2, "item_id": 103, "rating": 5},
    {"user_id": 2, "item_id": 104, "rating": 3},
    {"user_id": 2, "item_id": 105, "rating": 2},
    {"user_id": 2, "item_id": 106, "rating": 4},

    {"user_id": 3, "item_id": 105, "rating": 4},
    {"user_id": 3, "item_id": 101, "rating": 3},
    {"user_id": 3, "item_id": 107, "rating": 5},
    {"user_id": 3, "item_id": 108, "rating": 2},

    {"user_id": 4, "item_id": 102, "rating": 2},
    {"user_id": 4, "item_id": 103, "rating": 4},
    {"user_id": 4, "item_id": 106, "rating": 5},
    {"user_id": 4, "item_id": 109, "rating": 3},

    {"user_id": 5, "item_id": 104, "rating": 5},
    {"user_id": 5, "item_id": 105, "rating": 3},
    {"user_id": 5, "item_id": 110, "rating": 4},
    {"user_id": 5, "item_id": 101, "rating": 2},

    {"user_id": 6, "item_id": 108, "rating": 3},
    {"user_id": 6, "item_id": 109, "rating": 5},
    {"user_id": 6, "item_id": 110, "rating": 4},
    {"user_id": 6, "item_id": 102, "rating": 3},

    {"user_id": 7, "item_id": 106, "rating": 4},
    {"user_id": 7, "item_id": 107, "rating": 5},
    {"user_id": 7, "item_id": 108, "rating": 2},
    {"user_id": 7, "item_id": 110, "rating": 3}
]

# Create DataFrame
user_ratings = pd.DataFrame(data)
