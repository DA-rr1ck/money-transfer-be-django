from django.urls import path
from .views import LoginAPI, TransferAPI

urlpatterns = [
    path('login/', LoginAPI.as_view(), name='api_login'),
    path('transfer/', TransferAPI.as_view(), name='api_transfer'),
]
