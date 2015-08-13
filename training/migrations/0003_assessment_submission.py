# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20150812_1453'),
        ('training', '0002_element'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(max_length=1000)),
                ('tag', models.CharField(unique=True, max_length=10)),
                ('deadline', models.DateTimeField(default=datetime.datetime(2015, 8, 12, 21, 40, 31, 800444))),
                ('element', models.OneToOneField(to='training.Element')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(null=True, upload_to=b'', blank=True)),
                ('URL', models.URLField(blank=True)),
                ('assessment', models.ForeignKey(to='training.Assessment')),
                ('researcher', models.ForeignKey(to='profiles.Researcher')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
