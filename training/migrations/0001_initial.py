# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20150812_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('tag', models.CharField(max_length=10)),
                ('description', models.TextField(max_length=1000)),
                ('start', models.DateField(default=datetime.date.today)),
                ('accommodation', models.TextField(max_length=1000, blank=True)),
                ('module_map', models.TextField(max_length=1000, blank=True)),
                ('pic', sorl.thumbnail.fields.ImageField(default=b'module_img/default.jpg', upload_to=b'module_img')),
                ('coordinator', models.OneToOneField(to='profiles.Academic')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
