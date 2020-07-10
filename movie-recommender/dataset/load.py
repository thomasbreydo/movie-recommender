import pandas as pd


def rename_id_to_movieId(cols):
    new = list(cols)
    new[new.index('id')] = 'movieId'
    return new


def load_movies():
    try:
        ratings = pd.read_csv('ratings.csv')
        meta = pd.read_csv('movies_metadata.csv')
    except FileNotFoundError:
        raise FileNotFoundError(
            'make sure you download The Movie Dataset from Kaggle')
    meta.columns = rename_id_to_movieId(meta.columns)
    meta['movieId'] = pd.to_numeric(
        meta.loc[meta['movieId'].str.isnumeric(), 'movieId'])
    return pd.merge(ratings, meta, on='movieId')
