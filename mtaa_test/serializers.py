from rest_framework import serializers

from mtaa_test.models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name', 'create_time', 'owner']