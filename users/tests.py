from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views

from .forms import ConnexionForm
from .views import login, logout, signup, account


class StatusCodePageTestCase(TestCase):

    def setUp(self):
        self.cli = Client()

    def test_login(self):
        rep = self.cli.get('users/login')
        self.assertEqual(rep.status_code, 200)

    def test_logout(self):
        rep = self.cli.get('/users/logout')
        self.assertEqual(rep.status_code, 200)

    def test_signup(self):
        rep = self.cli.get('/users/signup')
        self.assertEqual(rep.status_code, 200)

    def test_account(self):
        rep = self.cli.get('/users/account')
        self.assertEqual(rep.status_code, 302)


class UserAuthenticateTestCase(TestCase):
    def setUp(self):
        self.cli = Client()
        user_test = Users.objects.create_user(
            username='testUser',
            password='longpasswordtest'
        )
        user_test.save()
        self.user = user_test

    def test_user_not_login_with_view(self):
        rep = self.cli.post('/users/login',
            {'user': 'notUser', 'password': 'longpasswordtest'}
        )
        # self.assertTrue(rep.form.errors)

    def test_user_login(self):
        rep = self.cli.get('/users/login')
        self.assertEqual(rep.status_code, 200)

    def test_user_redirect_after_login(self):
        rep = self.cli.post('/users/login',
            {'user': 'testUser', 'password': 'longpasswordtest'}
        )
        self.assertEqual(rep.status_code, 302)

    def test_user_is_authenticated(self):
        rep = self.cli.login(username='testUser', password='longpasswordtest')
        self.assertTrue(rep)

        rep2 = self.cli.get('/users/login')
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
        rep = self.cli.post('/users/signup',
            {
                'username': 'secondary_user',
                'password1': 'longpasswordtest'
                'password2': 'longpasswordtest'
            }
        )
        self.assertEqual(rep.context['new_user'].username, 'secondary_user')

    def test_user_logout(self):
        self.cli.login(username=self.user.username,
            password='longpasswordtest'
        )
        rep = self.cli.get('/user/logout')
        user_logout = rep.user.is_anonymous
        self.assertTrue(user_logout)

    def test_informations_for_account_user_page(self):
        self.cli.login(username=self.user.username,
            password='longpasswordtest'
        )
        rep = self.cli.get('/user/account')
        self.assertEqual(rep.context['pseudo'], self.user.username)

class FormTestCase(TestCase):
    def test_form_signup(self):
        form_data = {
            'username': 'testUser',
            'password1': 'longpasswordtest'
            'password2': 'longpasswordtest'
        }
        form = UserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_login(self):
        form_data = {
            'username': 'testUser',
            'password': 'longpasswordtest',
        }
        form = auth_views.LoginView(data=form_data)
        self.assertTrue(form.is_valid())


class TemplateRenderTestCase(TestCase):
    def setUp(self):
        self.cli = Client()
        user_test = User.objects.create_user(
            username='testUser',
            password='test'
        )
        user_test.save()
        self.cli.login(username=user_test.username, password=user_test.password)

    def test_template_login(self):
        rep = self.cli.get('/users/login')
        self.assertTemplateUsed(rep, 'users/login.html')

    def test_template_signup(self):
        rep = self.cli.get('/users/signup')
        self.assertTemplateUsed(rep, 'users/signup.html')

    def test_template_account(self):
        rep = self.cli.get('/users/account')
        self.assertTemplateUsed(rep, 'users/account.html')


class ViewsUsedTestCase(TestCase):
    def setUp(self):
        self.cli = Client()

    # def test_views_login(self):
    #     rep = self.cli.get('/users/login')
    #     self.assertEqual(rep.resolver_match.func, login)

    def test_views_signup(self):
        rep = self.cli.get('/users/signup')
        self.assertEqual(rep.resolver_match.func, signup)

    # def test_views_logout(self):
    #     rep = self.cli.get('/users/logout')
    #     self.assertEqual(rep.resolver_match.func, logout)

    def test_views_account(self):
        rep = self.cli.get('/users/account')
        self.assertEqual(rep.resolver_match.func, account)