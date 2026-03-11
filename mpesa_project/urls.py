# mpesa_project/urls.py
from django.contrib import admin           # ✅ Import admin here
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),      # Now admin is defined
    path('api/mpesa/', include('mpesa.urls')),  # Your app URLs
]