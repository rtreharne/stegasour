from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from training.models import Module

def core_level_training(request):
    modules = Module.objects.order_by('start')[:]

    return render(request, 'core_level_training.html', {'modules': modules})



