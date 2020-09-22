from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views

from ..views import signup, account


class UserAuthenticateTestCase(TestCase):
    def setUp(self):
        self.cli = Client()
        user_test = User.objects.create_user(
            username='testUser',
            password='longpasswordtest'
        )
        user_test.save()
        self.user = user_test

    def test_user_not_login_with_view(self):
        self.cli.logout()
        rep = self.cli.post('/users/login/',
            {'username': 'notUser', 'password': 'longpasswordtest'}
        )
        self.assertTrue(self.user.is_authenticated)

    def test_user_login(self):
        rep = self.cli.get('/users/login/')
        self.assertEqual(rep.status_code, 200)

    def test_user_redirect_after_login(self):
        rep = self.cli.post('/users/login/',
            {'username': 'testUser', 'password': 'longpasswordtest'}
        )
        self.assertEqual(rep.status_code, 302)

    def test_user_is_authenticated(self):
        rep = self.cli.login(username='testUser', password='longpasswordtest')
        self.assertTrue(rep)

        rep2 = self.cli.get('/users/login/')
        self.assertEqual(rep2.context['user'].get_username(), 'testUser')

    def test_user_is_not_authenticated(self):
        rep = self.cli.login(username='notUser', password='notPwd')
        self.assertFalse(rep)
    
    def test_user_signup(self):
        user_test2 = User.objects.create_user(
            username='testUser2',
            password='test'
        )
        user_test2.save()
        rep = User.objects.get(username__contains='testUser2')
        self.assertEqual(rep.username, 'testUser2')

    def test_user_signup_with_view(self):
        rep = self.cli.post('/users/signup/',
            {
                'username': 'user_test_creation',
                'password1': 'longpasswordtest',
                'password2': 'longpasswordtest'
            }
        )
        user_test = User.objects.get(username='user_test_creation')
        self.assertEqual(user_test.username, 'user_test_creation')

    def test_user_logout(self):
        self.cli.login(username=self.user.username,
            password='longpasswordtest'
        )
        rep = self.cli.get('/users/logout/')
        user_logout = self.user.is_anonymous
        self.assertFalse(user_logout)

    def test_informations_for_account_user_page(self):
        self.cli.login(username=self.user.username,
            password='longpasswordtest'
        )
        rep = self.cli.get('/users/account/')
        self.assertEqual(rep.context['pseudo'], self.user.username)

