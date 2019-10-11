from django.shortcuts import render

# Create your views here.
from million.models import *
from million.serializers import *
from rest_framework import generics
from rest_framework.response import *
from django.http import Http404
from rest_framework.views import APIView


class SexView(generics.ListCreateAPIView):
	queryset=Sex.objects.all()
	serializer_class=Sex_Serializers