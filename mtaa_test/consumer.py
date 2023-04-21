# chat/consumers.py
import json

from mtaa_test.models import Account, Room, Message
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message_content = text_data_json["message"]
        sender_id = text_data_json["sender_id"]
        room_id = text_data_json["room_id"]

        # Get the related Account and Room instances
        account_instance = Account.objects.get(id=sender_id)
        room_instance = Room.objects.get(id=room_id)

        # Save the received message to the database
        message_instance = Message(text=message_content, account=account_instance, room=room_instance)
        message_instance.save()

        self.send(text_data=json.dumps({"message": text_data_json, }))