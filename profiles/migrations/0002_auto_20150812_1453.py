# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Researcher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('bio', models.TextField(max_length=2000, blank=True)),
                ('pic', sorl.thumbnail.fields.ImageField(default=b'static/img/avatar.png', upload_to=b'researcher_images')),
                ('url', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('linkedIn', models.URLField(blank=True)),
                ('affiliation', models.ForeignKey(to='profiles.Partner')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='academic',
            name='pic',
            field=sorl.thumbnail.fields.ImageField(default=b'static/img/avatar.png', upload_to=b'academic_images'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='academic',
            name='affiliation',
            field=models.ForeignKey(to='profiles.Partner'),
        ),
    ]
