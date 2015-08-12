from django.db import models
from sorl.thumbnail import ImageField

class Partner(models.Model):
    name = models.CharField(max_length=128)
    logo = ImageField(upload_to='logos')

    def __unicode__(self):
        return self.name

class Academic(models.Model):
    title = models.CharField(max_length=5)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    affiliation = models.ForeignKey(Partner)
    bio = models.TextField(max_length=2000, blank=True)
    pic = ImageField(upload_to='academic_images', default='static/img/avatar.png')
    url = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedIn = models.URLField(blank=True)

    def __unicode__(self):
        return self.last_name

class Researcher(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    affiliation = models.ForeignKey(Partner)
    bio = models.TextField(max_length=2000, blank=True)
    pic = ImageField(upload_to='researcher_images', default='static/img/avatar.png')
    url = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedIn = models.URLField(blank=True)

    def __unicode__(self):
        return self.last_name

