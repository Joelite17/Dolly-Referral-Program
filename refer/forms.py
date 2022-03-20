from email import message
from django import forms
from .models import *
from account.models import *


class AccountActivationForm(forms.ModelForm):
    class Meta:
        model = AccountActivation
        fields = ('Payer_Wallet_Address',)


class FeedbackMessageForm(forms.ModelForm):

    class Meta:
        model = FeedbackMessage
        fields = ('message',)


class WithdrawalRequestForm(forms.ModelForm):

    class Meta:
        model = WithdrawalRequest
        fields = ('USDT_Amount',)


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name']


class WalletProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = WalletProfile
        fields = ['wallet_address']
