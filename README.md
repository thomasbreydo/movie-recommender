# movie-recommender
This project uses machine learning to suggest movies for a user.

<!-- # How it works
The model . . .
- gathers info about movies you liked
- finds similarities in your preferences and those of other users
- **finds movies for you to watch** -->

# How to use
## Before starting
- Download the csv files from [The Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset) on Kaggle into `./movie-recommender/dataset/`.
## Rate some movies by hand
The model will need to know about your movie preferences! All notebooks for this section are found in  `./movie-recommender/rate-movies/`.

- Open `get_movies_for_user_to_rate.ipynb` run all cells to create and save a list of ~200 titles for you to rate.
- Open `rate_movies.ipynb` and run all cells. The second-to-last cell will ask you to rate the ~200 movies.
    - The last cell saves your progress at any point during your rating process! To load saved progress, restart the kernel and run all cells again.

# Create your personal recommender!