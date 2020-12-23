import pytest
import requests

base_url = 'https://swapi.dev/api'


# task1: create fixture which will return the array of all people
@pytest.fixture()
def api_get_people():
    next_page = base_url + '/people/'
    people = []
    while (next_page is not None):
        response = requests.get(next_page)
        assert response.status_code == 200
        people += response.json()['results']
        next_page = response.json()['next']
    return people


# task7: create fixture which will return schema of people object
@pytest.fixture()
@pytest.mark.skip("wrong documentation")
def api_get_schema_people_obj():
    response = requests.get(base_url + '/people/schema/')
    assert response.status_code == 200
    return response.json()


@pytest.fixture()
def api_get_schema_people_obj_ok():
    response = requests.get(base_url + '/people/schema')
    assert response.status_code == 200
    return response.json()


# task9: create factory fixture which will return search people result
@pytest.fixture()
def api_get_search_result():
    def _api_get_search_result(arg):
        response = requests.get(base_url + '/people/?search=' + arg)
        assert response.status_code == 200
        return response.json()

    return _api_get_search_result
