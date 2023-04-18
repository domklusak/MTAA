from django.urls import re_path

from mtaa_test import consumer

websocket_urlpatterns = [
    re_path(r'ws/room/', consumer.ChatConsumer.as_asgi()),
]