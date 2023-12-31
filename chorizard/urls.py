"""
URL configuration for chorizard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include, path

from .chores import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("oidc/", include("mozilla_django_oidc.urls")),
    path("chores/", include("chorizard.chores.urls", namespace="chores")),
    path("family/", include("chorizard.family.urls", namespace="family")),
    path("", views.HomeView.as_view()),
]
