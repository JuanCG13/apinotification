# core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotificationsViews

router = DefaultRouter()
router.register(r'notifications', NotificationsViews)

urlpatterns = [
    path("", include(router.urls))
]