import json

import pytest
import requests

PATCH_URL = "https://jsonplaceholder.typicode.com/posts/100"
@pytest.fixture(scope="module")
def patch_post():
    payload = {"title": "test_TAU_patch"}
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    response = requests.patch(PATCH_URL, data=json.dumps(payload),
                              headers=headers)
    yield response
    requests.delete(PATCH_URL, headers=headers)