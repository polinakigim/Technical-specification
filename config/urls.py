from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "network/", include("electronics_network.urls", namespace="electronics_network")
    ),
]
