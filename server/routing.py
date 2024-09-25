from django.urls import path
from .consumers import TestConnectionConsumer

websocket_urlpatterns = [
  path('connect/', TestConnectionConsumer.as_asgi()),
]
