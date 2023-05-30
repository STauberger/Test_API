import pytest
import requests
from jsonschema import validate

def test_api_status_code(base_url):
    response = requests.get(base_url)
    assert response.status_code == 200


def test_brewery_schema(base_url):
    response = requests.get(f"{base_url}/breweries")
    assert response.status_code == 200
    data = response.json()[0]
    assert "id" in data
    assert "name" in data
    assert "brewery_type" in data
    assert "street" in data
    assert "city" in data
    assert "state" in data
    assert "postal_code" in data
    assert "country" in data
    assert "longitude" in data
    assert "latitude" in data
    assert "phone" in data
    assert "website_url" in data


def test_brewery_by_id(base_url, id=1):
    response = requests.get(f"{base_url}/breweries/{id}")
    assert response.status_code == 200
    assert response.json()["id"] == id


@pytest.mark.parametrize("id", [1, 2, 3, 4, 5])
def test_brewery_ids(base_url, id):
    test_brewery_by_id(base_url, id)


def test_brewery_search(base_url):
    response = requests.get(f"{base_url}/breweries/search?query=dog")
    assert response.status_code == 200

def test_schema_brewereis(base_url):
    response = requests.get(f"{base_url}/breweries")
    assert response.status_code == 200
    resp = response.json()
    schema = {
        "type": "array",
        "items": {
            "type": "object"
        }
    }
    validate(resp, schema)

