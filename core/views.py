# core/views.py

from rest_framework.generics import CreateAPIView
from rest_framework import viewsets
from core.serializers import NotificationSerializer
from .models import Notifications
from core.sendmail.mail import MailNotification

import requests
import threading

class NotificationsViews(viewsets.ModelViewSet):

    serializer_class = NotificationSerializer
    queryset = Notifications.objects.all()

    


    # def get_serializer(self, *args, **kwargs):
    #     # leave this intact
    #     serializer_class = self.get_serializer_class()
    #     kwargs["context"] = self.get_serializer_context()

    #     """
    #     Intercept the request and see if it needs tweaking
    #     """
    #     # if (name := self.request.data.get("name")) and (
    #     #     surname := self.request.data.get("surname")
    #     # ):

    #         #
    #         # Copy and manipulate the request
    #     draft_request_data = self.request.data.copy()
    #     # draft_request_data["name"]
    #     # draft_request_data["email"] = email
    #     # draft_request_data["phone"] = phone_number

    #     print('hola entre en la funcion')

    #     kwargs["data"] = draft_request_data
    #     return serializer_class(*args, **kwargs)
    #     """
    #     If not mind your own business and move on
    #     """
    #     return serializer_class(*args, **kwargs)

    # other = Notifications.objects.all().last()
    # print(other)
    # MailNotification(other)


    # def sendmail(request):
    #     if request.method == 'POST':
    #         name = request.POST.get('name')
    #         email = request.POST.get('email')
    #         phone = request.POST.get('phone')

    #         message = 'Nombre: ',name,'/nEmail: ',email,'/nNumero de telefono: ',phone
    #         MailNotification(message)


# def printit():
#     threading.Timer(1.0, printit).start()
#     url = "https://recetasapi.herokuapp.com/api/recipes/" 
#     response = requests.get(url)        # To execute get request 
#     print(response.status_code)     # To print http response code  
#     print(response.text)

# printit()