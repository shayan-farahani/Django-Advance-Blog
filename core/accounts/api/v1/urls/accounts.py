from django.contrib import admin
from django.urls import path, include
from .. import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    # registrations
    path(
        "registrations/",
        views.RegistrationsApiViews.as_view(),
        name="registrations",
    ),
    path(
        "token/login/",
        views.CustomObtainAuthToken.as_view(),
        name="token-login",
    ),
    path(
        "token/logout/",
        views.CustomDiscardAuthToken.as_view(),
        name="token-logout",
    ),
    path(
        "jwt/create/",
        views.CustomTokenObtainPairView.as_view(),
        name="jwt-create",
    ),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path(
        "change-password",
        views.ChangePasswordApiView.as_view(),
        name="change-password",
    ),
    path(
        "activations/confirm/<str:token>",
        views.ActivationApiView.as_view(),
        name="activation",
    ),
    path(
        "activations/resend/",
        views.ActivationResendApiView.as_view(),
        name="activation-resend",
    ),
    path("test", views.TestEmailSend.as_view(), name="test"),
]
