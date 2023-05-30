import pytest
import requests
from jsonschema import validate

# проверяет, что API возвращает картинку случайной собаки, а также проверяет, что возвращаемый URL картинки начинается с "https://".

def test_random_dog(base_url):
    response = requests.get(f'{base_url}/breeds/image/random')
    assert response.status_code == 200
    assert 'https://' in response.json()['message']

# проверяет, что API возвращает все породы собак
def test_all_breeds(base_url):
    response = requests.get(f'{base_url}/breeds/list/all')
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
# проверяет, что API возвращает подпороды для определенной породы собак.
def test_sub_breed(base_url):
    breed = 'hound'
    response = requests.get(f'{base_url}/breed/{breed}/list')
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert len(response.json()['message']) > 0
# параметризованный тест, проверяет, что API возвращает определенное количество случайных картинок собак.
@pytest.mark.parametrize("count", [1, 3, 5])
def test_random_dog_count(base_url, count):
    response = requests.get(f'{base_url}/breeds/image/random/{count}')
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert len(response.json()['message']) == count

# параметризованный тест, проверяет, что API возвращает картинки для каждой породы собак, указанной в списке.

@pytest.mark.parametrize("breed", ['hound', 'akita', 'beagle'])
def test_breed_images(base_url, breed):
    response = requests.get(f'{base_url}/breed/{breed}/images')
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert len(response.json()['message']) > 0

# проверяет что отображаются не более 50 фото собак

    @pytest.mark.parametrize("number", [50, 51, 345, 999, pytest.param(0, marks=pytest.mark.xfail)])
    def test_limit_50(number, base_url, get_image):
        run_limit = f"{base_url}/{get_image}/{number}"
        dogs_limit = requests.get(run_limit)
        assert len(dogs_limit.json().get("message")) == 50

    def test_breed_list(base_url):
        response = requests.get(f"{base_url}/breed/hound/images")
        assert response.status_code == 200

        schema = {
            "type": "object",
            "properties": {
                "message": {"type": "array"},
                "status": {"type": "string"}
            },
            "required": ["message", "status"]
        }
        validate(instance=response.json(), schema=schema)
