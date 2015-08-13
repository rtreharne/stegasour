from django.db import models
from datetime import datetime
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User

class Article(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=128)
    date = models.DateTimeField(default = datetime.now())
    body = models.TextField(blank=True, max_length=10000)
    upload_image = ImageField(upload_to='blog_img', blank=True, null=True)
    
    def __unicode__(self):
        return self.title

