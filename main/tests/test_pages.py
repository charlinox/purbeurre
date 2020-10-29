from django.test import TestCase, Client
from ..views import legalmention, index


class StatusCodePageTestCase(TestCase):
    def setUp(self):
        self.cli = Client()

    def test_page_index(self):
        rep = self.cli.get('/main/')
        self.assertEqual(rep.status_code, 200)

    def test_page_legal_mention(self):
        rep = self.cli.get('/main/')
        self.assertEqual(rep.status_code, 200)
