from django.test import TestCase, Client
from django.contrib.auth.models import User

from ..views import save_food, my_food
from products.models import Category, Product


class StatusCodePageTestCase(TestCase):
    def setUp(self):
        self.cli = Client()

    def test_page_save_food(self):
        rep = self.cli.get('/')
        self.assertEqual(rep.status_code, 200)

    def test_page_my_food(self):
        rep = self.cli.get('/')
        self.assertEqual(rep.status_code, 200)
