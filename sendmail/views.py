from django.shortcuts import render
from sendmail.models import Notification
from sendmail.mail import MailNotification
import requests
import threading
import json

# Create your views here.

def index(request):
    return render(request,'index.html')


def printit():
    threading.Timer(10.0, printit).start()
    url = "localhost:8000/api/notifications/" 
    # To execute get request 
    response = requests.get(url)
    print('entre en la funcion')

    print(Notification.objects.all())

    convert = json.loads(response.text)
    longitud = len(convert)
    print(convert)

    # if longitud != len(Notification.objects.all()):
    #     user = Notification(cantidad=longitud)
    #     user.save()
    #     longitud = longitud - 1
    #     nombre = convert[longitud]['name']
    #     email = convert[longitud]['email']
    #     numero = convert[longitud]['phone_number']
    #     cadena = ' Nombre: ' + str(nombre) + '\n Email: '+ str(email) + '\n Numero de telefono: '+ str(numero)
    #     MailNotification(cadena)
    #     print(cadena)
        

printit()