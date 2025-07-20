
# File: mydjango_projects/my_tennis_club/members/urls.py
from django.urls import path
from . import views  #

urlpatterns = [
     path('', views.main, name='main'),
     path('', views.members, name='members'),
     path('details/<int:id>', views.details, name='details'),
]