from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from training.models import *
from django.core.exceptions import ObjectDoesNotExist
from training.forms import SubmitAssessmentForm
from profiles import *

def core_level_training(request):
    modules = Module.objects.order_by('start')[:]

    return render(request, 'core_level_training.html', {'modules': modules})

def core_module(request, module_id=1):

	student = False
	submissions = None

	module = Module.objects.get(id=module_id)
	elements = Element.objects.filter(module=module)

	if request.user.is_authenticated():
		resources = Resource.objects.filter(element=elements).order_by('name')
		try:
			Researcher.objects.get(user=request.user)
			student = True
			submissions = Submission.objects.filter(researcher=request.user, assessment__element__module = module)
		except ObjectDoesNotExist:
			student = False
	else:
		resources = Resource.objects.filter(element=elements, public='1').order_by('name')


	assessments = Assessment.objects.filter(element=elements)


	mod_dict = {'module': module,
			    'elements': elements,
				'resources': resources,
				'assessments': assessments,
				'submissions': submissions,
				'student': student}


	return render(request, 'core-module.html', mod_dict)

@login_required
def submit_assessment(request, module_id=1, assessment_id=1):
    assessment = Assessment.objects.get(id = assessment_id)

    if request.method =="POST":
        submission_form = SubmitAssessmentForm(data=request.POST)

        if submission_form.is_valid():
            submission = submission_form.save(commit=False)
            submission.researcher = Researcher.objects.get(user=request.user)
			
            submission.assessment = assessment
			
            if 'file' in request.FILES:
                submission.file = request.FILES['file']

                submission.save()
                return HttpResponseRedirect('/training/core-level/%s' % (module_id))

        else:
            print upload_form.errors

    else:
        submission_form = SubmitAssessmentForm()

	return render(request, 'submit_assessment.html', {'submission_form': submission_form, 'assessment': assessment})




