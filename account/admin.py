from django.contrib import admin
from .models import *


@admin.register(WalletProfile)
class WithdrawalRequestAdmin(admin.ModelAdmin):
    list_display = ("user", "wallet_address",)
