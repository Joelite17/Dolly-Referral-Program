from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.


def homepage(request):

    return render(request, 'crypto/homepage.html')
