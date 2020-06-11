# core/admin.py

from django.contrib import admin
from .models import Notifications  # add this
# Register your models here.

admin.site.register(Notifications) # add this