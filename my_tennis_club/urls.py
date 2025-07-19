
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Welcome to My Tennis Club!")

urlpatterns = [
   # path('', home, name='home'),  # URL pattern for the home view
    path('members/', include('members.urls')),  # Include the members app URLs
    path('admin/', admin.site.urls),
]
