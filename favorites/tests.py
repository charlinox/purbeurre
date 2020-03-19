from django.test import TestCase, Client
from .views import save_food, my_food
from products.models import Category, Product
from django.contrib.auth.models import User


class StatusCodePageTestCase(TestCase):
    def setUp(self):
        self.cli = Client()

    def test_page_save_food(self):
        rep = self.cli.get('/')
        self.assertEqual(rep.status_code, 200)

    def test_page_my_food(self):
        rep = self.cli.get('/')
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

        user_test = User.objects.create_user(
            username='testUser',
            password='longpasswordtest'
        )
        user_test.save()
        self.user = user_test
        self.cli.login(username='testUser', password='longpasswordtest')


    def test_views_my_food(self):
        rep = self.cli.get('/favorites/my_food/')
        self.assertEqual(rep.resolver_match.func, my_food)

    def test_views_save_food(self):
        rep = self.cli.get('/favorites/save_food/')
        self.assertEqual(rep.resolver_match.func, save_food)
