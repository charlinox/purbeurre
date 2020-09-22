from django.test import TestCase, Client

from ..views import signup, account


class StatusCodePageTestCase(TestCase):

    def setUp(self):
        self.cli = Client()

    def test_login(self):
        rep = self.cli.get('/users/login/')
        self.assertEqual(rep.status_code, 200)

    def test_signup(self):
        rep = self.cli.get('/users/signup/')
        self.assertEqual(rep.status_code, 200)

    def test_account(self):
        rep = self.cli.get('/users/account/')
        self.assertEqual(rep.status_code, 302)
