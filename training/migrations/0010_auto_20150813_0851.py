# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0009_auto_20150813_0833'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('feedback', models.TextField(blank=True)),
                ('score', models.DecimalField(max_digits=4, decimal_places=1, blank=True)),
                ('upload', models.FileField(null=True, upload_to=b'submission/feedback/', blank=True)),
                ('submission', models.ForeignKey(to='training.Submission')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 8, 51, 20, 792118)),
        ),
        migrations.AlterField(
            model_name='submission',
            name='file',
            field=models.FileField(null=True, upload_to=b'submission', blank=True),
        ),
    ]
