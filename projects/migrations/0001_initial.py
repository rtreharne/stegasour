# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=8)),
                ('tag', models.CharField(max_length=8)),
                ('start', models.DateField(default=datetime.date.today)),
                ('finish', models.DateField(default=datetime.date.today)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(max_length=10000, blank=True)),
                ('cohort', models.OneToOneField(to='projects.Cohort')),
                ('supervisor1', models.ForeignKey(related_name=b'supervisor1', to='profiles.Academic')),
                ('supervisor2', models.ForeignKey(related_name=b'suptervisor2', to='profiles.Academic')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
