from django.db import models


class Account(models.Model):
    password = models.TextField(max_length=255)
    tag = models.TextField(max_length=255)
    balance = models.FloatField()
    name = models.TextField(max_length=255)
    surname = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    friends = models.ManyToManyField("self")
    claims = models.ManyToManyField("DebtsClaims")
    transactions = models.ManyToManyField("Transaction")
    rooms = models.ManyToManyField("Room")


class DebtsClaims(models.Model):
    amount = models.FloatField()
    debt_account = models.ForeignKey(Account, models.DO_NOTHING, related_name="dc_account1")


class Room(models.Model):
    name = models.TextField(max_length=255)
    create_time = models.DateField(auto_now=True)
    owner = models.ForeignKey(Account, models.DO_NOTHING, null=True)


class Message(models.Model):
    text = models.TextField(max_length=255)
    send_time = models.DateTimeField(auto_now=True)
    account = models.ForeignKey(Account, models.DO_NOTHING)
    room = models.ForeignKey(Room, models.DO_NOTHING)


class Transaction(models.Model):
    amount = models.FloatField()  # This field type is a guess.
    note = models.TextField(blank=True, null=True)
    time = models.DateTimeField(auto_now=True)
    dest_account = models.ForeignKey(Account, models.DO_NOTHING, related_name="transaction")

