from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from profiles.models import *

def user_login(request):
    invalid = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('dashboard'))
            else:
                return HttpResponse("Your account is disabled")

        else:
            invalid = True 
            return render(request, 'login.html', {'invalid': invalid})
                
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'login.html', {'invalid': invalid})

def dashboard(request):
    try:
        profile = Researcher.objects.get(user=request.user)
    except ObjectDoesNotExist:
        profile = Academic.objects.get(user=request.user)

    return render(request, 'dashboard.html', {'profile': profile})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
