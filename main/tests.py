from django.test import TestCase, Client
from products.models import Category, Product
from .views import legalmention, index


class StatusCodePageTestCase(TestCase):
    def setUp(self):
        self.cli = Client()

    def test_page_index(self):
        rep = self.cli.get('/main/')
        self.assertEqual(rep.status_code, 200)

    def test_page_legal_mention(self):
        rep = self.cli.get('/main/')
        self.assertEqual(rep.status_code, 200)


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

    def test_views_legalmention(self):
        rep = self.cli.get('/main/mention_legale')
        self.assertEqual(rep.resolver_match.func, legalmention)

    def test_views_index(self):
        rep = self.cli.get('/main/')
        self.assertEqual(rep.resolver_match.func, index)
