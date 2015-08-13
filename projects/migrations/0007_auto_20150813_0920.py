# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_academic_role'),
        ('projects', '0006_project_researcher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=128)),
                ('upload', models.FileField(null=True, upload_to=b'upload', blank=True)),
                ('URL', models.URLField(blank=True)),
                ('researcher', models.ForeignKey(to='profiles.Researcher')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Upload_Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='upload',
            name='type',
            field=models.ForeignKey(to='projects.Upload_Type'),
            preserve_default=True,
        ),
    ]
