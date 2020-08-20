# api/urls.py
from django.contrib import admin
from django.urls import path, include        # add this
from django.conf import settings             # add this
from django.conf.urls.static import static   # add this
from sendmail.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include('core.urls')),       # add this
    path('index/', index)
]

# add this
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)