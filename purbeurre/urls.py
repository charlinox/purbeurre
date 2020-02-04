from django.contrib import admin
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("products/", include("products.urls")),
]
