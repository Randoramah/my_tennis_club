
# File: mydjango_projects/my_tennis_club/members/urls.py
from django.urls import path
from . import views  #

urlpatterns = [
    path('', views.members, name='members'),  # URL pattern for the members view
]