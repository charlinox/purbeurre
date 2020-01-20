from django.urls import path

from . import views

urlpatterns = [
    path('user_connexion/', views.user_connexion, name='user_connexion'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('user_signup/', views.user_signup, name='user_signup'),
]