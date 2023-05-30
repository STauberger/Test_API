import pytest
import requests


@pytest.fixture(scope="module")
def base_url():
    return "https://api.openbrewerydb.org/breweries"


@pytest.fixture(scope="module")
def status_code():
    return 200


@pytest.fixture(scope="module")
def error_status_code():
    return 404


def test_check_brewery_api(base_url, status_code):
    response = requests.get(base_url)
    assert response.status_code == status_code


@pytest.mark.parametrize("id", [1000000, "test", -1])
def test_negative_brewery_api(base_url, id, error_status_code):
    response = requests.get(f"{base_url}/{id}")
    assert response.status_code == error_status_code
