import os

import requests
from gensim.models import Word2Vec


ENV_ENDPOINT_NAME = 'ML_DATASTORE_ENDPOINT'
API_ENDPOINT = os.getenv(ENV_ENDPOINT_NAME, None)
if API_ENDPOINT is None:
    raise EnvironmentError(
        'There is no API endpoint path. '
        'Please, provide {} environment variable'.format(ENV_ENDPOINT_NAME))
API_ENDPOINT = API_ENDPOINT.rstrip('/')


def get_word_vector(word: str) -> Word2Vec:
    vector_raw_data = requests.get('{}/{}'.format(API_ENDPOINT, word))
    return Word2Vec(vector_raw_data)
