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

class Upload_Type(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name
    
class Upload(models.Model):
    type = models.ForeignKey(Upload_Type)
    researcher = models.ForeignKey(Researcher)
    label = models.CharField(max_length=128)
    upload = models.FileField(upload_to='upload', null=True, blank=True)
    URL = models.URLField(blank=True)
    CHOICE = (
        (u'1', u'YES'),
        (u'2', u'NO'),
    )
    public = models.CharField(max_length=3, choices=CHOICE, default=CHOICE[0][0])

    def __unicode__(self):
        return '%s_%s_%s' % (self.label, self.researcher.last_name, self.type.name)
    

    
