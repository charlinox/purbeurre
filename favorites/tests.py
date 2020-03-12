from django.test import TestCase, Client


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

    def test_views_my_food(self):
        rep = self.cli.get('/my_food')
        self.assertEqual(rep.resolver_match.func, my_food)

    def test_views_save_food(self):
        rep = self.cli.get('/save_food')
        self.assertEqual(rep.resolver_match.func, save_food)
