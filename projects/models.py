from django.db import models
from datetime import datetime, date
from profiles.models import Academic, Researcher

class Cohort(models.Model):
    name = models.CharField(max_length=8)
    tag = models.CharField(max_length=8)
    start = models.DateField(default=date.today)
    finish = models.DateField(default=date.today)

    def __unicode__(self):
        return self.name

class Project(models.Model):
    supervisor1 = models.ForeignKey(Academic, related_name='supervisor1')
    supervisor2 = models.ForeignKey(Academic, related_name='supervisor2', null=True, blank=True)
    researcher = models.OneToOneField(Researcher, null=True, blank=True)
    title = models.CharField(max_length=500)
    cohort = models.ForeignKey(Cohort)
    description = models.TextField(max_length = 10000, blank=True)
    attachment = models.FileField(upload_to='projects', blank=True, null=True)
    
    def __unicode__(self):
        return self.title
    

    
