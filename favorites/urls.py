from django.urls import path

from . import views


urlpatterns = [
    path('save_food', views.save_food, name='save_food'),
    path('my_food', views.my_food, name='my_food'),
]
