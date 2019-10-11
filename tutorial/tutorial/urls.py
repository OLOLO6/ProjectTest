from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from million import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('million.urls'))
]
