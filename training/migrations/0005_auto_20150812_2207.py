# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0004_auto_20150812_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('upload', models.FileField(null=True, upload_to=b'resources/', blank=True)),
                ('URL', models.URLField(blank=True)),
                ('element', models.ForeignKey(to='training.Element')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resource_Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='resource',
            name='resource_type',
            field=models.ForeignKey(to='training.Resource_Type'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='assessment',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 12, 22, 7, 32, 566622)),
        ),
    ]
