import json
import requests as rq
from pprint import pprint
from deepdiff import DeepDiff

from .base import Base
from .api import get_cad_data


def find_changes(saved_data, new_data):
    if DeepDiff(new_data, saved_data):
        print('New data detected!')
        pprint(DeepDiff(new_data, saved_data))
        print('New data successful saved to base!')
    else:
        print('Saved data is up to date!')
