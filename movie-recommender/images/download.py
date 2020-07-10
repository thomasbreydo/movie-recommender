# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import requests
import shutil
import apikeys
import os
from tqdm import tqdm


# %%
SAVEDIR = 'posters'


# %%
def construct_request_url(imdb_id):
    return f'https://img.omdbapi.com/?apikey={apikeys.OMDb}&i={imdb_id}'


# %%
def save_poster(respose, savepath):
    with open(savepath, 'wb') as f:
        shutil.copyfileobj(respose.raw, f)


# %%
def download_poster(imdb_id, savepath):
    if not os.path.exists(savepath):
        request_url = construct_request_url(imdb_id)
        save_poster(requests.get(request_url, stream=True), savepath)
