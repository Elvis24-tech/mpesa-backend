from django.urls import path
from .views import stk_push, mpesa_callback

urlpatterns = [
    path('stkpush/', stk_push, name='stkpush'),
    path('callback/', mpesa_callback, name='callback'),  # <-- add this
]