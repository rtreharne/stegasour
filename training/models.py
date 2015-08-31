from django.db import models
from profiles.models import Academic, Researcher
from datetime import date
from sorl.thumbnail import ImageField
from datetime import datetime
from profiles.models import Partner

class Module(models.Model):
    name = models.CharField(max_length=128)
    location = models.ForeignKey(Partner)
    tag = models.CharField(max_length=10)
    description = models.TextField(max_length=1000)
    coordinator = models.OneToOneField(Academic)
    start = models.DateField(default=date.today)
    finish = models.DateField(default=date.today)
    accommodation = models.TextField(max_length=1000, blank=True)
    module_map = models.TextField(max_length=1000, blank=True)
    pic = ImageField(upload_to='module_img', default = 'module_img/default.jpg')

    def __unicode__(self):
        return self.name

class Element(models.Model):
    title = models.CharField(max_length=128)
    module = models.ForeignKey(Module)
    description = models.TextField(max_length=1000)
    tag = models.CharField(max_length=10, unique=True)

    def __unicode__(self):
        return '%s (%s)' % (self.title, self.module.tag)

class Assessment(models.Model):
    element = models.OneToOneField(Element)
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=1000)
    tag = models.CharField(max_length=10, unique=True)
    deadline = models.DateTimeField(default=datetime.now())
    points = models.IntegerField(default=30)

    def __unicode__(self):
        return '%s (%s)' % (self.title, self.element.module.tag)

class Submission(models.Model):
    assessment = models.ForeignKey(Assessment)
    researcher = models.ForeignKey(Researcher)
    file = models.FileField(upload_to='submission', blank=True, null=True)
    URL = models.URLField(blank = True)

    def __unicode__(self):
        return '%s_%s' % (self.assessment.title, self.researcher.last_name)

class Resource_Type(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name

class Resource(models.Model):
    name = models.CharField(max_length=128, unique=True)
    element = models.ForeignKey(Element)
    resource_type = models.ForeignKey(Resource_Type)
    upload = models.FileField(upload_to='resources/', blank=True, null=True)
    URL = models.URLField(blank=True)
    embed = models.CharField(max_length=5000, blank=True, null=True)
    CHOICE = (
        (u'1', u'YES'),
        (u'2', u'NO'),
    )
    public = models.CharField(max_length=3, choices=CHOICE, default=CHOICE[0][0])

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.element.module.tag)

class Feedback(models.Model):
    submission = models.ForeignKey(Submission)
    feedback = models.TextField(blank=True)
    score = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    upload = models.FileField(upload_to='submission/feedback/', blank=True, null=True)

    def __unicode__(self):
        return '%s_%s (%s)' % (self.submission.assessment.title, self.submission.researcher.last_name, self.submission.assessment.element.module.name)
        
    


    


    

