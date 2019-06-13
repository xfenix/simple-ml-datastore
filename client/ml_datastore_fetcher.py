import os

import requests
from gensim.models import Word2Vec


ENV_ENDPOINT_NAME = 'ML_DATASTORE_ENDPOINT'
API_ENDPOINT = os.getenv(ENV_ENDPOINT_NAME, 'http://127.0.0.1:8000/')
if API_ENDPOINT is None:
    raise EnvironmentError(
        'There is no API endpoint path. '
        'Please, provide {} environment variable'.format(ENV_ENDPOINT_NAME))
API_ENDPOINT = API_ENDPOINT.rstrip('/')
LOCAL_CACHE = {}


def get_word_vector(word: str) -> Word2Vec:
    if word in LOCAL_CACHE:
        vector_raw_data = LOCAL_CACHE[word]
    else:
        vector_raw_data = requests.get('{}/{}'.format(API_ENDPOINT, word)).text.rstrip()
        LOCAL_CACHE[word] = vector_raw_data
    return Word2Vec(vector_raw_data)
