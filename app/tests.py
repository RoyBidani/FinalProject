import unittest
import requests
from bs4 import BeautifulSoup

class TestMyFlaskApp(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://localhost:5000'  

    def test_site_is_up(self):
        response = requests.get(self.base_url)
        self.assertEqual(response.status_code, 200)

    def test_error_pages(self):
        response = requests.get(f"{self.base_url}/aaa")
        self.assertEqual(response.status_code, 404)
        response = requests.get(f"{self.base_url}/read/aaa")
        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()

