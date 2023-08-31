import unittest
from urllib.request import urlopen
import json

class TestGitHubAPI(unittest.TestCase):

    def setUp(self):
        # Define the URL
        self.url = "https://api.github.com"

        # Fetch and parse the JSON data
        self.response = urlopen(self.url)
        self.data_json = json.loads(self.response.read())

    def test_response_status_code(self):
        self.assertEqual(self.response.status, 200)

    def test_response_data_type(self):
        self.assertIsInstance(self.data_json, dict)

    def test_response_has_keys(self):
        required_keys = ['current_user_url', 'current_user_authorizations_html_url', 'authorizations_url', 'code_search_url']
        for key in required_keys:
            self.assertIn(key, self.data_json)

    def test_response_key_values(self):
        self.assertEqual(self.data_json['current_user_url'], "https://api.github.com/user")
        self.assertEqual(self.data_json['authorizations_url'], "https://api.github.com/authorizations")
        self.assertEqual(self.data_json['code_search_url'], "https://api.github.com/search/code?q={query}{&page,per_page,sort,order}")

if __name__ == '__main__':
    unittest.main()
