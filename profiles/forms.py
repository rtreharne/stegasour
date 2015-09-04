from django import forms
from django.contrib.auth.models import User
from profiles.models import *
from projects.models import Project, Upload

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['pic'].label = 'Picture'

    class Meta:
        model = Academic
        fields = ('user','affiliation', 'pic', 'bio', 'url', 'linkedIn', 'twitter')

class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ('title', 'description', 'supervisor1', 'supervisor2')

class AddPortfolioForm(forms.ModelForm):
    
    class Meta:
        model = Upload
        fields = ('type', 'label', 'upload', 'URL', 'public')

class EditPortfolioForm(forms.ModelForm):
    
    class Meta:
        model = Upload
        fields = ('type', 'label', 'upload', 'URL', 'public')
