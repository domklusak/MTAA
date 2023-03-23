from rest_framework import serializers

from mtaa_test.models import Room
from mtaa_test.models import Account
from mtaa_test.models import Transaction
from mtaa_test.models import DebtsClaims


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name', 'create_time', 'owner']


class AccountSerializer(serializers.ModelSerializer):
    friends = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all(), many=True)
    claims = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all(), many=True)
    transactions = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all(), many=True)
    class Meta:
        model = Account
        fields = ['id', 'password', 'tag', 'balance', 'name', 'surname', 'email', 'friends', 'claims', 'transactions']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'note', 'time', 'dest_account']

class DebtsClaimsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebtsClaims
        fields = ['id', 'amount', 'debt_account']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'text', 'send_time', 'account', 'room']