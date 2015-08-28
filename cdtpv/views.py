from django.shortcuts import render
from django.contrib.auth.models import User
from projects.models import Project, Cohort
from profiles.models import Academic

def home(request):
	return render(request, 'home.html', {})

def researchers(request):
    projects = Project.objects.order_by('researcher__last_name')[:]
    cohorts = Cohort.objects.all()
    return render(request, 'researchers.html', {'projects': projects, 'cohorts': cohorts})

def academics(request):
    academics = Academic.objects.order_by('last_name')[:]
    return render(request, 'academics.html', {'academics': academics})

