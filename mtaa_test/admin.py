from django.contrib import admin
from mtaa_test.models import Account
# Register your models here.

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass