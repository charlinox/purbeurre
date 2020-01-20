from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse

from . import views

urlpatterns = [
    # path('user_connexion/', views.user_connexion, name='user_connexion'),
    path('user_connexion/', auth_views.login, {'template_name': 'users/connexion.html'}),
    # path('user_logout/', views.user_logout, name='user_logout'),
    path('user_logout/', auth_views.login, {'template_name': reverse(user_connexion)}),
    # ??? on peut faire comme ca avec reverse ???
    path('user_signup/', views.user_signup, name='user_signup'),
]
