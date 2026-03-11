# mpesa_app/urls.py
from django.urls import path
from .views import stk_push

urlpatterns = [
    path('stkpush/', stk_push, name='stkpush'),
]