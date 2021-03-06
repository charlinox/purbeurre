from django.test import TestCase, Client
from ..models import Category, Product
from ..views import result, DetailView


class StatusCodePageTestCase(TestCase):
    def setUp(self):
        self.cli = Client()
        cat = Category()
        cat.name = 'conserves'
        cat.save()
        alim = Product()
        alim.id = 3245412718649
        alim.name = 'abricots'
        alim.save()
        alim.categories.add(cat)
        alim.save()

        self.food = alim

    def test_page_result(self):
        rep = self.cli.get('/')
        self.assertEqual(rep.status_code, 200)

    def test_page_food_detail(self):
        rep = self.cli.get(f'/products/food_detail/{self.food.id}/')
        self.assertEqual(rep.status_code, 200)

    def test_page_no_search(self):
        rep = self.cli.get(f'/products/no_search/')
        self.assertEqual(rep.status_code, 200)
