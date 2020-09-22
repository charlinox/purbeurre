from django.test import TestCase, Client
from ..models import Category, Product
from ..views import result, DetailView


class CheckViewsTestCase(TestCase):
    def setUp(self):
        self.cli = Client()
        cat = Category()
        cat.name = 'conserves'
        cat.save()
        alim = Product()
        alim.id = '3245412718649'
        alim.name = 'abricots'
        alim.save()
        alim.categories.add(cat)
        alim.save()
        self.food = alim

    def test_views_result(self):
        rep = self.cli.get('/products/result/')
        self.assertEqual(rep.resolver_match.func, result)

    def test_views_food_detail(self):
        rep = self.cli.get(f'/products/food_detail/{self.food.id}/')
        self.assertEqual(
            rep.resolver_match.func.__name__,
            DetailView.as_view().__name__
        )

    def test_views_result_no_search(self):
        rep = self.cli.get('/products/result/', {'research' : 'pate chocolat'})
        self.assertTemplateNotUsed(rep, '/products/result/')

