from django.urls import path

from . import views


urlpatterns = [
    path('save_food', views.savefood, name='save_food'),
    path('my_food', views.myfood, name='my_food'),
]
