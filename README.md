````markdown
# Recommendation System

This is a comprehensive **Recommendation System** that provides both **Collaborative Filtering** and **Content-Based Filtering** for **Movies** and **Books**. The system allows users to receive personalized recommendations based on their preferences and user ratings.

## Features

- **Collaborative Filtering**: Recommends items based on user ratings and preferences. The system builds a utility matrix to provide recommendations tailored to users.
  
- **Content-Based Filtering**: Recommends items based on item features like **Genre**, **Actor(s)**, and **Director(s)**. This method filters and suggests movies/books similar to those the user has shown interest in.

- **GUI Interface**: A user-friendly **Tkinter**-based graphical user interface (GUI) that allows users to easily interact with the recommendation system by providing inputs and viewing results.

- **Supports Movies and Books**: Users can choose to get recommendations for either **Movies** or **Books**.

## Technologies Used

- **Python**: The core programming language for this application.
- **Tkinter**: For the graphical user interface (GUI).
- **Pandas**: For handling data, especially for creating and processing user ratings and item data.
- **Custom Recommender Algorithms**: Implements both Collaborative and Content-Based filtering using custom algorithms and datasets.

## Installation

To get started with the recommendation system, follow these steps:

### 1. Clone the repository

```
git clone https://github.com/yourusername/recommendation-system.git
cd recommendation-system
````

### 2. Install dependencies

Make sure you have Python 3.x installed. Then, install the required libraries:

```
pip install -r requirements.txt
```

### 3. Running the Application

Once the dependencies are installed, you can run the application by executing:

```
python gui_app.py
```

The Tkinter-based GUI will launch, allowing you to input your user ID, choose between **Collaborative Filtering** or **Content-Based Filtering**, and specify genres, actors, or directors for more personalized recommendations.

## How to Use

1. **Enter User ID**: Provide a valid user ID from the dataset.
2. **Choose Recommendation Type**: Select between **Collaborative Filtering** or **Content-Based Filtering**.
3. **Choose Movie or Book**: Specify if you want recommendations for **Movies** or **Books**.
4. **Enter Genre (Optional)**: Optionally filter recommendations by **Genre**.
5. **Enter Actor(s) (Optional)**: For Content-Based filtering, you can specify the actor(s) (comma-separated).
6. **Enter Director (Optional)**: Optionally filter by **Director**.

Click the **Submit** button to generate recommendations.

## Datasets

The application uses the following sample datasets:

* **Movies Dataset**: A list of movies with attributes like **Title**, **Genre**, **Actors**, and **Director**.
* **Books Dataset**: A list of books with attributes like **Title**, **Genre**, **Authors**.
* **User Ratings**: A dataset containing user ratings for movies and books.

## Contributing

If you want to contribute to the project, feel free to fork the repository, make changes, and submit a pull request. We welcome contributions in the form of bug fixes, new features, and improvements!

## Contact

For any questions or issues, please feel free to open an issue in the repository or contact me directly.

---

**Sayan Karmakar**
[GitHub Profile](https://github.com/Stressed-by-a-mountain-of-codes)

```
