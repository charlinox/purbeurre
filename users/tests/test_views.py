from django.test import TestCase, Client

from ..views import signup, account


class ViewsUsedTestCase(TestCase):
    def setUp(self):
        self.cli = Client()

    def test_views_signup(self):
        rep = self.cli.get('/users/signup/')
        self.assertEqual(rep.resolver_match.func, signup)

    def test_views_account(self):
        rep = self.cli.get('/users/account/')
        self.assertEqual(rep.resolver_match.func, account)