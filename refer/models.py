from doctest import BLANKLINE_MARKER
from django.db.models import Max
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User

from account.models import WalletProfile

# from account.models import WalletProfile
from .utils import generate_ref_code
from django.urls import reverse

STATUS = (
    (0, "Disapproved"),
    (1, "Approved"),
    (2, "Denied"),
)


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,)
    code = models.CharField(max_length=12, blank=True)
    recommended_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name='ref_by')
    updated = models.DateTimeField(auto_now=True)
    earn = models.IntegerField(default=4)

    created = models.DateTimeField(auto_now_add=True)

    def get_recommened_profiles(self):
        global my_recs
        qs = Profile.objects.all()
        my_recs = []
        recs_user = []
        for profile in qs:
            if profile.recommended_by == self.user:
                my_recs.append(profile)
                recs_user.append(profile.user)
        return my_recs

    def referral_counter(self):
        qs = Profile.objects.all()
        my_recs_count = 0
        for profile in qs:
            if profile.recommended_by == self.user:
                my_recs_count += 1
        return my_recs_count

    def total_referral_counter(self):
        global counter
        qs = AccountActivation.objects.all()
        counter = 0
        # activated_list = []
        for address in qs:
            if address.status == 1:
                # activated_list.append(address.user.username)
                counter += 1

        return counter

    def total_earn(self):
        total_amount = 0
        counter = self.activated_referral_counter()
        if counter > 0:
            total_amount = (counter * 3) + 4

        return total_amount

    def __str__(self):
        return f"{self.user.username} {self.code}"

    def save(self, *args, **kwargs):
        if self.code == "":
            code = generate_ref_code()
            self.code = code
        super().save(*args, **kwargs)

    def activated_list(self):
        qs = AccountActivation.objects.all()
        activated_list = []
        for account in qs:
            if account.status == 1:
                activated_list.append(account.user)
        return activated_list


class AccountActivation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Payer_Wallet_Address = models.CharField(max_length=47)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"{self.user}"

    def save(self, *args, **kwargs):
        profiles = Profile.objects.all()
        if self.status == 1:
            for p in profiles:
                if self.user.profile.recommended_by == p.user:
                    recommender = Profile.objects.get(user=p.user)
                    Profile.objects.filter(user=p.user).update(
                        earn=recommender.earn+3)
        super().save(*args, **kwargs)

    def sent_activation_request(self):
        if self:
            if self.status == 1:
                return True
            else:
                return False

    def activated_referral_counter(self):
        num = 0
        account_activations = AccountActivation.objects.all()
        qs = Profile.objects.all()
        my_recs = []
        for profile in qs:
            if profile.recommended_by == self.user:
                my_recs.append(profile.user.username)
        for account_activation in account_activations:
            if account_activation.user.username in my_recs and account_activation.status == 1:
                num += 1

        return num

    def activated_referral_list(self):
        qs = AccountActivation.objects.all()
        activated_list = []
        for account in qs:
            if account.status == 1:
                activated_list.append(account)
        return activated_list


class FeedbackMessage(models.Model):
    message = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message}"


STATUS2 = (
    (0, "Not Confirmed"),
    (1, "Confirmed"),
)


class WithdrawalRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    USDT_Amount = models.PositiveIntegerField(
        validators=[MinValueValidator(20, "Minimum_Withdrawal $20")])
    wallet_address = models.CharField(max_length=47)
    status = models.IntegerField(choices=STATUS2, default=0)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"
