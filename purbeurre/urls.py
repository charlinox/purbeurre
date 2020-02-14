from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("main.urls")),
    path("admin/", admin.site.urls),
    path("main/", include("main.urls")),
    path("users/", include("users.urls")),
    path("products/", include("products.urls")),
    path("favorites/", include("favorites.urls")),
]
