from django.shortcuts import render, redirect, get_object_or_404
from refer.models import *
from refer.forms import *
from refer.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def referred(request):
    profile = Profile.objects.get(user=request.user)
    my_recs = profile.get_recommened_profiles()
    context = {'my_recs': my_recs}
    return render(request, 'refer/my_recs.html', context)


def referral_homepage(request, *args, **kwargs):
    code = str(kwargs.get('ref_code'))
    try:
        profile = Profile.objects.get(code=code)
        request.session['ref_profile'] = profile.id
        print('id', profile.id)
        return redirect('homepage')
    except:
        pass
    print(request.session.get_expiry_age())
    return render(request, 'crypto/homepage.html', {})


@login_required
def dashboard(request, *args, **kwargs):
    code = str(kwargs.get('ref_code'))
    try:
        profile = Profile.objects.get(code=code)
        request.session['ref_profile'] = profile.id
        print('id', profile.id)
    except:
        pass

    print(request.session.get_expiry_age())

    # Objects.all()
    profiles = Profile.objects.all()
    account_activations = AccountActivation.objects.all()
    withdrawal_request = WithdrawalRequest.objects.all()
    # Objects.all()

    # Objects.get()

    account_activation = None
    activated_referral_counter = 0
    profile = Profile.objects.get(user=request.user)
    if request.user in profile.activated_list():
        account_activation = AccountActivation.objects.get(
            user=request.user)
        activated_referral_counter = account_activation.activated_referral_counter()

    withdrawal_request = WithdrawalRequest.objects.filter(
        user=request.user)
    wallet_profile = WalletProfile.objects.get(user=request.user)

    # End Object.get()

    # Model Properties
    referral_counter = profile.referral_counter()

    # End Model

    # Variable for loop or if statement
    new_message = None
    new_withdrawal = None
    # End Variable

    # Varibles for display and hiding of referral link
    sent_activation_request = False
    activate_account = False
    deny_account = False
    unactivate_account = False
    # End Variable

    # For account activation menu display and disappear
    for x in AccountActivation.objects.all():
        if request.user == x.user:
            sent_activation_request = True
    # End

    # For Activate account in dashboard
    for x in AccountActivation.objects.all():
        if request.user == x.user and x.status == 1:
            activate_account = True
    # End

    # For Unactivate account in dashboard
    for x in AccountActivation.objects.all():
        if request.user == x.user and x.status == 0:
            unactivate_account = True
    # End

    # For Denied account in dashboard
    for x in AccountActivation.objects.all():
        if request.user == x.user and x.status == 2:
            deny_account = True
    # End

    # Post requst
    if request.method == 'POST':
        message_form = FeedbackMessageForm(data=request.POST)
        if message_form.is_valid():
            # Create Comment object but don't save to daTabase yet
            new_message = message_form.save(commit=False)
            # Save the comment to the database
            new_message.save()
            messages.success(
                request, f'Thank you for messaging us')
            return redirect("dashboard")

    else:
        message_form = FeedbackMessageForm()

    if request.method == 'POST':
        withdrawal_form = WithdrawalRequestForm(data=request.POST)
        if withdrawal_form.is_valid():
            USDT_Amount = int(request.POST.get('USDT_Amount'))
            if USDT_Amount > profile.earn:
                messages.warning(
                    request, f'The amount requested is greater than the total earning')
                redirect("dashboard")
            else:
                balance = profile.earn - USDT_Amount
                wallet_address = wallet_profile.wallet_address
                withdrawal_request = WithdrawalRequest.objects.create(
                    user=request.user, USDT_Amount=USDT_Amount, wallet_address=wallet_address)
                withdrawal_request.save()
                Profile.objects.filter(user=request.user).update(earn=balance)

                messages.success(
                    request, f'Your request will be processed within 72 hours')
                return redirect("dashboard")

    else:
        withdrawal_form = WithdrawalRequestForm()
    # End Post request

    template_name = 'refer/dashboard.html'

    context = {'profiles': profiles, account_activation: account_activation,
               "referral_counter": referral_counter,
               #    "new_message": new_message,
               "message_form": message_form,
               #    "new_withdrawal": new_withdrawal,
               "withdrawal_form": withdrawal_form,
               "sent_activation_request": sent_activation_request,
               "profile": profile,
               "activate_account": activate_account,
               "unactivate_account": unactivate_account,
               "deny_account": deny_account,
               "activated_referral_counter": activated_referral_counter,
               "total_earning": profile.earn,
               "expenses": withdrawal_request,

               }
    return render(request, template_name, context)


@login_required
def settings(request):
    # wallet_addresses = AccountActivation.objects.get(user=request.user)
    profiles = Profile.objects.all()
    wallet_addresses = AccountActivation.objects.all()
    sender = request.user.username
    profile = Profile.objects.get(user=request.user)

    # true_account = wallet_addresses.true_account()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = WalletProfileUpdateForm(
            request.POST, instance=request.user.walletprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!!!')
            return redirect('settings')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = WalletProfileUpdateForm(instance=request.user.walletprofile)

# removal or adding of the activation account of the referral
    sent_activation_request = False
    for x in AccountActivation.objects.all():
        if request.user == x.user:
            sent_activation_request = True
    # End

    # For Activate account in dashboard
    activate_account = False
    for x in AccountActivation.objects.all():
        if request.user == x.user and x.status == 1:
            activate_account = True
    # End
    return render(request, 'refer/settings.html', {"u_form": u_form, "p_form": p_form,

                                                   #  "true_account": true_account,
                                                   'profiles': profiles,
                                                   'profile': profile,
                                                   "wallet_addresses": wallet_addresses,
                                                   "sender": sender,
                                                   "sent_activation_request": sent_activation_request,
                                                   "activate_account": activate_account,
                                                   })


@login_required
def withdrawal_history(request):
    # removal or adding of the activation account of the referral
    sent_activation_request = False
    for x in AccountActivation.objects.all():
        if request.user == x.user:
            sent_activation_request = True
    # End
    withdrawal_request = WithdrawalRequest.objects.filter(
        user=request.user).order_by('-pk')
    profile = Profile.objects.get(user=request.user)

    return render(request, 'refer/withdrawal_history.html', {
        "withdrawal_request": withdrawal_request,
        "sent_activation_request": sent_activation_request,
        "balance": profile.earn

    })


@login_required
def myreferrals(request):
    # activated referral and non activated referral detail start

    sender = request.user.username
    profile = Profile.objects.get(user=request.user)
    my_recs = profile.get_recommened_profiles()
    referral_counter = profile.referral_counter()

    wallet_addresses = None
    sent_activation_request = False
    my_activated_recs = []
    not_activated_recs = []
    my_total_recs = []
    my_recs_count = 0
    activated_list = None
    # total_earning = 0
    for x in AccountActivation.objects.all():
        if x.user == request.user:
            wallet_addresses = AccountActivation.objects.get(
                user=request.user)
            activated_list = wallet_addresses.activated_referral_list()

            if my_recs:
                for i in my_recs:
                    for a in activated_list:
                        if i.user == a.user:
                            my_activated_recs.append(a.user)
                            my_total_recs.append(a.user)
                my_recs_count = len(my_activated_recs)
            # total_earning = my_recs_count * 3
                for b in my_recs:
                    if b.user not in my_total_recs:
                        not_activated_recs.append(b.user)
                        my_total_recs.append(b.user)

    # End

    # removal or adding of the activation account of the referral
    for x in AccountActivation.objects.all():
        if request.user == x.user:
            sent_activation_request = True
    # End
    context = {'my_recs': my_recs,
               "referral_counter": referral_counter,
               "wallet_addresses": wallet_addresses,
               "sender": sender,
               "activated_list": activated_list,
               "my_recs_count": my_recs_count,
               "my_activated_recs": my_activated_recs,
               "not_activated_recs": not_activated_recs,
               #    "activated_referrals": activated_referrals,
               #    "true_account": true_account
               "sent_activation_request": sent_activation_request,

               }
    return render(request, 'refer/myreferrals.html', context)


@login_required
def account_activation(request):
    profile = Profile.objects.get(user=request.user)
    wallet_addresses = AccountActivation.objects.all()
    sender = request.user.username
    # true_account = wallet_addresses.true_account()

    new_wallet = None
    if request.method == 'POST':
        wallet_form = AccountActivationForm(data=request.POST)
        if wallet_form.is_valid():
            new_wallet = request.POST.get('Payer_Wallet_Address')
            account_activation = AccountActivation.objects.update_or_create(
                user=request.user, Payer_Wallet_Address=new_wallet)
            # account_activation.save()

            messages.success(
                request, f'Thank you. Your account will be activated within 48 hours if payment is confirmed. Note that if the payment wasn"t not receive your account won"t be activated.')
            return redirect("dashboard")

    else:
        wallet_form = AccountActivationForm()

    # removal or adding of the activation account of the referral
    sent_activation_request = False
    for x in AccountActivation.objects.all():
        if request.user == x.user and x.status == 1:
            sent_activation_request = True
    # End
    template_name = 'refer/account_activation.html'

    return render(request, template_name, {"wallet_form": wallet_form,
                                           "new_wallet": new_wallet,
                                           "wallet_addresses": wallet_addresses,
                                           "sender": sender,
                                           "sent_activation_request": sent_activation_request
                                           #    "true_account": true_account
                                           })
