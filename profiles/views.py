from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from profiles.models import *
from projects.models import Project, Upload, Upload_Type
from training.models import *
from profiles.forms import ProfileForm, ProjectForm, AddPortfolioForm

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
    researcher=False
    academic=False
    portfolio=None
    submissions=None
    feedback = []
    try:
        profile = Researcher.objects.get(user=request.user)
        projects = Project.objects.get(researcher=profile)
        portfolio = Upload.objects.filter(researcher=profile)
        types = Upload_Type.objects.all()
        folio = {}
        submissions = Submission.objects.filter(researcher=profile)
        feedback = Feedback.objects.all()
        for type in types:
            folio[type.name] =  portfolio.filter(type=type)
        researcher = True
        portfolio = folio
    except ObjectDoesNotExist:
        profile = Academic.objects.get(user=request.user)
        projects = Project.objects.filter(supervisor1=profile)
        academic = True

    prof_dict = {'profile': profile, 
                 'projects': projects,
                 'academic': academic,
                 'researcher': researcher,
                 'portfolio': portfolio,
                 'submissions': submissions,
                 'feedback': feedback}
                 

    return render(request, 'dashboard.html', prof_dict)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def update_profile(request):
    submitted = False
    try:
        inst = Researcher.objects.get(user=request.user)
    except ObjectDoesNotExist:
        inst = Academic.objects.get(user=request.user)

    if request.method == 'POST':
        profile_form = ProfileForm(data=request.POST, instance=inst)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user= request.user

            if 'pic' in request.FILES:
                profile.pic= request.FILES['pic']

            profile.save()

            submitted=True

        else:
            print profile_form.errors
        
    else:
        profile_form = ProfileForm(instance=inst)
    
    return render(request, 'update_profile.html', {'profile_form': profile_form, 'submitted': submitted})

@login_required
def update_project(request):
    submitted = False
    try:
        inst = Project.objects.get(researcher=request.user)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('dashboard'))

    if request.method =='POST':
        project_form = ProjectForm(data=request.POST, instance=inst)
        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.save()

            submitted=True

        else:
            print project_form.errors

    else:
        project_form = ProjectForm(instance=inst)
            
    return render(request, 'update_project.html', {'project_form': project_form, 'submitted': submitted})

@login_required
def add_portfolio_item(request):
    submitted = False
    try:  
        inst = Project.objects.get(researcher=request.user)
    except ObjectDoesNotExist:
	    return HttpResponseRedirect(reverse('dashboard'))

    if request.method == 'POST':
        upload_form = AddPortfolioForm(data=request.POST)
        if upload_form.is_valid():
            upload = upload_form.save(commit=False)

            upload.researcher = inst.researcher

            if 'upload' in request.FILES:
                upload.upload = request.FILES['upload']

            upload.save()
			
            submitted = True

        else:
            print upload_form.errors

    else:
        upload_form = AddPortfolioForm()

	
    return render(request, 'add_portfolio_item.html', {'upload_form': upload_form, 'submitted': submitted})

@login_required
def delete_portfolio_item(request, upload_id=1):
    upload = Upload.objects.get(id=upload_id)
    upload.delete()
    return HttpResponseRedirect('/user/dashboard/#portfolio')


	    
			
