# mpesa_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({"status": "Mpesa backend running"})

urlpatterns = [
    path('', home),  # Root route
    path('admin/', admin.site.urls),
    path('api/mpesa/', include('mpesa.urls')),
]