# core/serializers.py

from rest_framework import serializers
from .models import Notifications 
import json
class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notifications
        fields = ("id", "name", "email", "phone_number")
        # print(model)