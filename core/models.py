
# core/models.py

from django.db import models
# Create your models here.

class Notifications(models.Model):

    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    phone_number = models.PositiveIntegerField()
    
    
    def __str__(self):
        return " {}".format(self.name, self.email)