from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # registrations
    path("", include("accounts.api.v1.urls.accounts")),
    path("profile/", include("accounts.api.v1.urls.profiles")),
]
