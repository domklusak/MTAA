from django.urls import path
from mtaa_test import consumer

websocket_urlpatterns = [
    path(r"ws/room/<str:room_id>", consumer.ChatConsumer.as_asgi()),
]