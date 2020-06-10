# core/views.py

from rest_framework import viewsets
from .serializers import NotificationSerializer
from .models import Notifications

class NotificationsViews(viewsets.ModelViewSet):



    serializer_class = Notifications
    queryset = Recipe.objects.all()