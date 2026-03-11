from django.urls import path
from .views import stkpush, mpesa_callback

urlpatterns = [
    path("stkpush/", stkpush),
    path("callback/", mpesa_callback),
]