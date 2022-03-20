from django.contrib import admin
from .models import *


@admin.register(AccountActivation)
class AccountActivationAdmin(admin.ModelAdmin):
    list_display = ("user", "Payer_Wallet_Address", "status")


@admin.register(WithdrawalRequest)
class WithdrawalRequestAdmin(admin.ModelAdmin):
    list_display = ("user", "USDT_Amount",
                    "wallet_address", "status")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "code", "recommended_by",
                    "earn")


admin.site.register(FeedbackMessage)
