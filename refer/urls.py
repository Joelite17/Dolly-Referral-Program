from django.urls import path
from refer.views import *

urlpatterns = [
    path('referred/', referred, name='referred'),
    path('dashboard/', dashboard, name='dashboard'),
    path('settings/', settings, name='settings'),
    path('myreferrals/', myreferrals, name='myreferrals'),
    path('account_activation/', account_activation, name='account_activation'),
    path('withdrawal_history/',
         withdrawal_history, name='withdrawal_history'),
    path('<str:ref_code>/', referral_homepage, name='referral_view'),




]
