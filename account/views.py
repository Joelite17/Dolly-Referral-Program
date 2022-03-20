from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
# extension from refer app
from refer.models import *


def signup(request):
    global request_user
    request_user = request
    profile_id = request.session.get('ref_profile')
    form = UserSignupForm(request.POST or None)
    if form.is_valid():
        if profile_id is not None:
            recommended_by_profile = Profile.objects.get(id=profile_id)
            instance = form.save()
            registered_user = User.objects.get(id=instance.id)
            registered_profile = Profile.objects.get(user=registered_user)
            registered_profile.recommended_by = recommended_by_profile.user

            # End Appending
            registered_profile.save()
            save_form = form.save()
            save_form.refresh_from_db()  # load the profile instance created by the signal
            save_form.walletprofile.wallet_address = form.cleaned_data.get(
                'wallet_address')
            save_form.save()

        else:
            save_form = form.save()
            save_form.refresh_from_db()  # load the profile instance created by the signal
            save_form.walletprofile.wallet_address = form.cleaned_data.get(
                'wallet_address')
            save_form.save()
        messages.success(
            request, f'Your account has been created!!! You are now able to login')
        return redirect('login')
    return render(request, 'account/signup.html', {'form': form,
                                                   })


@login_required
def profile(request):
    # wallet_addresses = AccountActivation.objects.get(user=request.user)
    # true_account = wallet_addresses.true_account()
    wallet_addresses = AccountActivation.objects.all()
    sender = request.user.username
    profiles = Profile.objects.all()
    profile = Profile.objects.get(user=request.user)

    sent_activation_request = False
    for x in AccountActivation.objects.all():
        if request.user == x.user:
            sent_activation_request = True
    profile = Profile.objects.get(user=request.user)

    # For Activate account in dashboard
    activate_account = False
    for x in AccountActivation.objects.all():
        if request.user == x.user and x.status == 1:
            activate_account = True
    # End
    return render(request, 'account/profile.html', {'profiles': profiles, 'profile': profile,
                                                    "wallet_addresses": wallet_addresses,
                                                    "sender": sender,
                                                    "sent_activation_request": sent_activation_request,
                                                    "activate_account": activate_account
                                                    # "true_account": true_account
                                                    })

    # profiles = Profile.objects.all()
    # profile = get_object_or_404(Profile, code=code)
    # if request == "POST"
    # return HttpResponseRedirect(profile.get_absolute_url())
    # context = {
    #     # for production
    #     # 'allowed_host': ALLOWED_HOSTS[0],

    #     # for deployment
    #     'profile': profile
    # }
