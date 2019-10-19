from django.urls import path
from million import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from django.conf.urls import url

urlpatterns=[
path('singers',views.SingersView.as_view()),
path('groups',views.GroupsView.as_view()),
path('concert',views.ConcertView.as_view()),
path('singers/<int:pk>',views.SingersDetails.as_view()),
path('groups/<int:pk>',views.GroupsDetails.as_view()),
path('concert/<int:pk>',views.ConcertDetails.as_view()),
]
urlpatterns=format_suffix_patterns(urlpatterns)