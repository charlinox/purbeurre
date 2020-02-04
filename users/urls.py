from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse

from . import views

urlpatterns = [
    # path('login/', views.login, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='users/connexion.html'), name="login"),
    # path('logout/', views.logout, name='logout'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse("login")), name="logout"),
    path('signup/', views.signup, name='signup'),
]
