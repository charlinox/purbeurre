from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("products/", include("products.urls")),
    path("main/", include("main.urls")),
    path("favorites/", include("favorites.urls")),
]
