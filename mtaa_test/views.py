from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from mtaa_test.models import Room
from mtaa_test.serializers import RoomSerializer
from mtaa_test.models import Account
from mtaa_test.serializers import AccountSerializer
from mtaa_test.models import Transaction
from mtaa_test.serializers import TransactionSerializer
from mtaa_test.models import DebtsClaims
from mtaa_test.serializers import DebtsClaimsSerializer
from mtaa_test.models import Message
from mtaa_test.serializers import MessageSerializer


class RoomViewSet(viewsets.ModelViewSet):

    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = []


    def list(self, request, *args, **kwargs):

        if request.query_params.getlist("room_ids"):
            room_ids = request.query_params.get('room_ids', '').split(',')
        else:
            room_ids = request.query_params.getlist("room_ids")

        queryset = self.get_queryset()
        if len(room_ids) > 0:
            queryset = queryset.filter(id__in=room_ids)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        queryset = self.get_queryset()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(instance)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        queryset = self.get_queryset()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        queryset = self.get_queryset()
        instance = get_object_or_404(queryset, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AccountViewSet(viewsets.ModelViewSet):

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = []


    def list(self, request, *args, **kwargs):
        if request.query_params.getlist("account_ids"):
            account_ids = request.query_params.get('account_ids', '').split(',')
        else:
            account_ids = request.query_params.getlist("account_ids")

        queryset = self.get_queryset()
        if len(account_ids) > 0:
            queryset = queryset.filter(id__in=account_ids)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        queryset = self.get_queryset()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(instance)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        queryset = self.get_queryset()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        queryset = self.get_queryset()
        instance = get_object_or_404(queryset, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DebtsClaimsViewSet(viewsets.ModelViewSet):

    queryset = DebtsClaims.objects.all()
    serializer_class = DebtsClaimsSerializer
    permission_classes = []


    def list(self, request, *args, **kwargs):

        if request.query_params.getlist("debt_claim_ids"):
            debt_claim_ids = request.query_params.get('debt_claim_ids', '').split(',')
        else:
            debt_claim_ids = request.query_params.getlist("debt_claim_ids")

        queryset = self.get_queryset()
        if len(debt_claim_ids) > 0:
            queryset = queryset.filter(id__in=debt_claim_ids)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        account_id = request.query_params.get("account_id")
        account = get_object_or_404(Account.objects.all(), pk=account_id)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            claims = serializer.save()
            account.claims.add(claims)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        queryset = self.get_queryset()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(instance)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        queryset = self.get_queryset()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        queryset = self.get_queryset()
        instance = get_object_or_404(queryset, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MessageViewSet(viewsets.ModelViewSet):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = []


    def list(self, request, *args, **kwargs):

        if request.query_params.getlist("message_ids"):
            message_ids = request.query_params.get('message_ids', '').split(',')
        else:
            message_ids = request.query_params.getlist("message_ids")

        queryset = self.get_queryset()
        if len(messsage_ids) > 0:
            queryset = queryset.filter(id__in=messsage_ids)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        queryset = self.get_queryset()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(instance)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        queryset = self.get_queryset()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        queryset = self.get_queryset()
        instance = get_object_or_404(queryset, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TransactionViewSet(viewsets.ModelViewSet):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = []


    def list(self, request, *args, **kwargs):

        if request.query_params.getlist("transaction_ids"):
            transaction_ids = request.query_params.get('transaction_ids', '').split(',')
        else:
            transaction_ids = request.query_params.getlist("transaction_ids")

        queryset = self.get_queryset()
        if len(transaction_ids) > 0:
            queryset = queryset.filter(id__in=transaction_ids)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        queryset = self.get_queryset()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(instance)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        account_id = request.query_params.get("account_id")
        account = get_object_or_404(Account.objects.all(), pk=account_id)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            transaction = serializer.save()
            account.transactions.add(transaction)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)