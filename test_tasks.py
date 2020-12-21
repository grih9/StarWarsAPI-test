import pytest
import requests
import string
import collections

base_url = 'https://swapi.dev/api'

# task2: create test which checks length of array of all people with "count" field in responce
def test_count_equals_len_of_array(api_get_people):
    response = requests.get(base_url + '/people/')
    assert response.status_code == 200
    count_field = response.json()['count']
    assert count_field == len(api_get_people)

# task3: create test which checks that names of all people are unique
def test_names_are_unique(api_get_people):
    dict_names = collections.Counter([name['name'] for name in api_get_people])
    names_count_values = set(dict_names.values())
    assert (1 in names_count_values) and (len(names_count_values) == 1)

# task4: create a few tests for validation that search for people is case insensitive
def equivalent_json_responses(resp_json1, resp_json2):
    assert resp_json1['count'] == resp_json2['count']
    for i in range(int(resp_json1['count'])):
        assert resp_json1['results'][i]['name'] == resp_json2['results'][i]['name']

@pytest.mark.parametrize('value1, value2', [('r2', 'R2'), ('darth', 'dARtH'), ('lars', 'LARS'), ('V', 'v')])
def test_search_people_case_insensitive(value1, value2):
    response1 = requests.get(base_url + '/people/?search=' + str(value1))
    assert response1.status_code == 200
    response2 = requests.get(base_url + '/people/?search=' + str(value2))
    assert response2.status_code == 200
    equivalent_json_responses(response1.json(), response2.json())


# task5: create test which will validate that there is no page with number 0 for people request
def test_no_page_0_people_req():
    response = requests.get(base_url + '/people/?page=0')
    assert response.status_code == 404
    response = requests.get(base_url + '/people/?page=1')
    assert response.json()['previous'] == None

# task6: create parametrized test which will check that there are 3 Skywalker's, 1 Vader, 2 Darth's (using ?search)
@pytest.mark.parametrize('count, name', [(3, 'Skywalker'), (1, 'Vader'), (2, 'Darth')])
def test_names_count(count, name):
    responce = requests.get(base_url + '/people/?search=' + name)
    assert responce.status_code == 200
    assert int(responce.json()['count']) == count
    assert len(responce.json()['results']) == count

# task8: create test which will validate that all people object contain required schema fields
@pytest.mark.skip("wrong documentation")
def test_people_obj_contain_required_schema(api_get_schema_people_obj, api_get_people):
    requiered_fields = set(api_get_schema_people_obj['required'])
    for creature in api_get_people:
        creature_fields = set(creature.keys())
        assert requiered_fields.issubset(creature_fields)

def test_people_obj_contain_required_schema_ok(api_get_schema_people_obj_ok, api_get_people):
    requiered_fields = set(api_get_schema_people_obj_ok['required'])
    for creature in api_get_people:
        creature_fields = set(creature.keys())
        assert requiered_fields.issubset(creature_fields)


# task10: create test which will check that search for any char in Eng alphabet
# or any number from 0 to 9 will return number of results > 0 except cases of
# search by 6, 9 and 0

test_arg = (string.ascii_lowercase + string.digits)
@pytest.mark.parametrize('test_arg', test_arg)
def test_search_any_char_not_empty_result(api_get_search_result, test_arg):
    res = api_get_search_result(test_arg)
    if test_arg not in '069':
        assert res['count'] > 0
        assert len(res['results']) > 0
    else:
        assert res['count'] == 0
        assert len(res['results']) == 0


