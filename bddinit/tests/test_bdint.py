# return_value
from django.test import TestCase
from unittest.mock import patch

from ..management.commands.bdinit import ProductDownloader

class FetchTestCase(TestCase):
    
    @patch('requests.get')
    def test_requests_get(self, mock_requests_get):
        
        class Response:
            def json(self):
                return {
                    "products": []
                }
        productDownloader = ProductDownloader()
        response = Response()
        mock_requests_get.return_value = response
        fetch_response = productDownloader.fetch("boissons", 500)
        self.assertEqual(fetch_response, response.json()["products"])
