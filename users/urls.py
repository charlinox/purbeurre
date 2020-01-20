from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse

from . import views

urlpatterns = [
    # path('user_connexion/', views.user_connexion, name='user_connexion'),
    path('connexion/', auth_views.LoginView.as_view(template_name='users/connexion.html'), name="user_connexion"),
    # path('user_logout/', views.user_logout, name='user_logout'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse("user_connexion")), name="user_logout"),
    path('signup/', views.user_signup, name='user_signup'),
]
