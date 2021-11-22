from django.urls import path
from .consumers import WSConsumer

websocket_urlpatterns = [
    path('', WSConsumer.as_asgi())
]