import pandas as pd
import os

BASEPATH = os.path.dirname(__file__)


def rename_id_to_movieId(cols):
    new = list(cols)
    new[new.index('id')] = 'movieId'
    return new


def try_load_csv(csvname, usecols=None):
    try:
        return pd.read_csv(os.path.join(BASEPATH, csvname), usecols=usecols)
    except FileNotFoundError:
        raise FileNotFoundError(
            'make sure you download The Movie Dataset from Kaggle')


def load_meta(usecols=None):
    meta = try_load_csv('movies_metadata.csv', usecols)
    meta.columns = rename_id_to_movieId(meta.columns)
    meta['movieId'] = pd.to_numeric(
        meta.loc[meta['movieId'].str.isnumeric(), 'movieId'])
    return meta


def load_ratings(usecols=None):
    return try_load_csv('ratings.csv', usecols)


def load_movies(ratingcols=None, metacols=None):
    # not using designated load functinos to avoid storing in memory many times
    ratings = load_ratings(ratingcols)
    meta = load_meta(metacols)
    return pd.merge(ratings, meta, on='movieId')
