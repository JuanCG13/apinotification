from django.db import models

# Create your models here.

class Notification (models.Model):
    cantidad = models.IntegerField(default=None)
    
    def __str__(self):
        return "{}".format(self.cantidad)