from django.contrib.auth.views import *
from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'),
         name='logout'),  # This is replaceable with the main app
]
