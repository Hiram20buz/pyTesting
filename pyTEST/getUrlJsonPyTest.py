import pytest
from urllib.request import urlopen
import json

# Define the URL
url = "https://api.github.com"

# Fetch and parse the JSON data
response = urlopen(url)
data_json = json.loads(response.read())

def test_response_status_code():
    assert response.status == 200

def test_response_data_type():
    assert isinstance(data_json, dict)

def test_response_has_keys():
    required_keys = ['current_user_url', 'current_user_authorizations_html_url', 'authorizations_url', 'code_search_url']
    for key in required_keys:
        assert key in data_json

def test_response_key_values():
    assert data_json['current_user_url'] == "https://api.github.com/user"
    assert data_json['authorizations_url'] == "https://api.github.com/authorizations"
    assert data_json['code_search_url'] == "https://api.github.com/search/code?q={query}{&page,per_page,sort,order}"
