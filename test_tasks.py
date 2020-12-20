import pytest
import requests
import collections

base_url = 'https://swapi.dev/api/'

# task2: create test which checks length of array of all people with "count" field in responce
def test_count_equals_len_of_array(api_get_people):
    response = requests.get(base_url + 'people/')
    assert response.status_code == 200
    count_field = response.json()['count']
    assert count_field == len(api_get_people)

# task3: create test which checks that names of all people are unique
def test_names_are_unique(api_get_people):
    dict_names = collections.Counter([name['name'] for name in api_get_people])
    names_count_values = set(dict_names.values())
    assert 1 in names_count_values
    assert len(names_count_values) == 1

# task4: create a few tests for validation that search for people is case insensitive
def equivalent_json_responses(resp_json1, resp_json2):
    assert resp_json1['count'] == resp_json2['count']
    for i in range(int(resp_json1['count'])):
        assert resp_json1['results'][i]['name'] == resp_json2['results'][i]['name']

@pytest.mark.parametrize('value1, value2', [('r2', 'R2'), ('darth', 'dARtH'), ('lars', 'LARS'), ('V', 'v')])
def test_search_people_case_insensitive(value1, value2):
    response1 = requests.get(base_url + 'people/?search=' + str(value1))
    assert response1.status_code == 200
    response2 = requests.get(base_url + 'people/?search=' + str(value2))
    assert response2.status_code == 200
    equivalent_json_responses(response1.json(), response2.json())
