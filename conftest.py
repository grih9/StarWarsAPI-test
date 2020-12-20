import pytest
import requests

base_url = 'https://swapi.dev/api/'

#@pytest.fixture()
#def test_fixture():
    # setup

#    yield
    # teardown

# task1: create fixture which will return the array of all people
@pytest.fixture()
def api_get_people():
    next_page = base_url + 'people/'
    people = []
    while (next_page is not None):
        response = requests.get(next_page)
        assert response.status_code == 200
        people += response.json()['results']
        next_page = response.json()['next']
    return people

