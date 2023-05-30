
import pytest

@pytest.fixture
def base_url():
    url = "https://dog.ceo/api"
    return url

@pytest.fixture
def get_image():
    endpoint = "breeds/image/random"
    return endpoint