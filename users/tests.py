from django.test import TestCase, Client


class SatusCodePageTestCase(TestCase):
    def setUp(self):
        self.cli = Client()

    def test_login(self):
        rep = self.cli.get('/')
        self.assertEqual(rep.status_code, 200)

    def test_logout(self):
        rep = self.cli.get('/')
        self.assertEqual(rep.status_code, 200)

    def test_signup(self):
        rep = self.cli.get('/')
        self.assertEqual(rep.status_code, 200)
