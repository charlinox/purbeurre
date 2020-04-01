from django.urls import path

from . import views

urlpatterns = [
    path("result/", views.result, name="result"),
    path("no_search/", views.result, name="no_search"),
    path('food_detail/<int:pk>/', views.DetailView.as_view(), name='food_detail'),
]
