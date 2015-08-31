from django import forms
from django.contrib.auth.models import User
from profiles.models import *
from training.models import *

class SubmitAssessmentForm(forms.ModelForm):
    
    class Meta:
        model = Submission
        fields = ('file', 'URL')
