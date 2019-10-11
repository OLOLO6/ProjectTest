from django.urls import path
from million import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from django.conf.urls import url

urlpatterns=[
path('sex',views.SexView.as_view()),
]
urlpatterns=format_suffix_patterns(urlpatterns)