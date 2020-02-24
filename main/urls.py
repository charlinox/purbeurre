from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('mention_legale', views.legalmention, name='legal_mention'),
    path('mention_legale', views.legalmention, name='legal_mention'),
]
