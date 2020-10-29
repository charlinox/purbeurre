from django.test import TestCase, Client
from django.contrib.auth.models import User

from ..views import signup, account


class TemplateRenderTestCase(TestCase):
    def setUp(self):
        self.cli = Client()
        user_test = User.objects.create_user(
            username='testUser',
            password='test'
        )
        user_test.save()
        self.user = user_test
        self.cli.login(username=self.user.username, password='test')

    def test_template_login(self):
        rep = self.cli.get('/users/login/')
        self.assertTemplateUsed(rep, 'users/login.html')

    def test_template_signup(self):
        self.cli.logout()
        rep = self.cli.get('/users/signup/')
        self.assertTemplateUsed(rep, 'users/signup.html')
        self.cli.login(username=self.user.username, password='test')

    def test_template_account(self):
        rep = self.cli.get('/users/account/')
        self.assertEqual(rep.status_code, 200)
        self.assertTemplateUsed(rep, 'users/account.html')
