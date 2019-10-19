from django.shortcuts import render

# Create your views here.
from million.models import *
from million.serializers import *
from rest_framework import generics
from rest_framework.response import *
from django.http import Http404
from rest_framework.views import APIView

import re
def PhoneValid(x: str):
    if len(x)>13:
        return False
    y=re.findall(r'\+996\d{9}',x)
    return len(y)>0


class SingersView(generics.ListCreateAPIView):
	queryset=Singers.objects.all()
	serializer_class=Singers_Serializers

class SingersDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = Singers.objects.all()
	serializer_class = Singers_Serializers

class GroupsView(generics.ListCreateAPIView):
	queryset=Groups.objects.all()
	serializer_class=Groups_Serializers
class GroupsDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = Groups.objects.all()
	serializer_class = Groups_Serializers

class ConcertView(generics.ListCreateAPIView):
	queryset=Concert.objects.all()
	serializer_class=Concert_Serializers
class ConcertDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = Concert.objects.all()
	serializer_class = Concert_Serializers