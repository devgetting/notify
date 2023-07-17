from django.urls import re_path
from .consumers.NotificationConsumer import NotificationConsumer

websocket_urlpatterns = [
    re_path(r'ws/notification/$', NotificationConsumer.as_asgi())
]