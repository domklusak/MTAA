from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

class Account(models.Model):
    password = models.TextField(max_length=255)
    tag = models.TextField(max_length=255)
    balance = models.FloatField()
    name = models.TextField(max_length=255)
    surname = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    user = models.OneToOneField(get_user_model(), on_delete=models.DO_NOTHING, related_name="account")
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


@receiver(pre_save, sender=Account)
def link_user(sender, instance, **kwargs):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(
            email=instance.email
        )
    except UserModel.DoesNotExist:
        user = UserModel(email=instance.email)
    user.set_password(instance.password)
    user.username = instance.email
    user.save()
    instance.user = user


