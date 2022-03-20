from enum import unique
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

from django.core.exceptions import ValidationError


class UserSignupForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=15, required=True)
    last_name = forms.CharField(max_length=15, required=True)
    wallet_address = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'wallet_address', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    # def clean_email(self):
    #     email = self.cleaned_data["email"]
    #     if User.objects.filter(email=email).exists():
    #         raise ValidationError("An user with this email already exists!")
    #     return email

# def clean_unique(form, field, exclude_initial=True,
            #  format="The %(field)s %(value)s has already been taken."):
#     value = form.cleaned_data.get(field)
#     if value:
#         qs = form._meta.model._default_manager.filter(**{field: value})
#         if exclude_initial and form.initial:
#             initial_value = form.initial.get(field)
#             qs = qs.exclude(**{field: initial_value})
#         if qs.count() > 0:
#             raise forms.ValidationError(
#                 format % {'field': field, 'value': value})
#     return value
