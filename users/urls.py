from django.urls import path

from . import views

urlpatterns = [
    path('connexion/', views.login, name='connexion'),
    path('deconnexion/', views.logout, name='deconnexion'),
    path('inscription/', views.login, name='signup'),
]