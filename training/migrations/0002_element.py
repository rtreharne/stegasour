# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(max_length=1000)),
                ('tag', models.CharField(unique=True, max_length=10)),
                ('module', models.ForeignKey(to='training.Module')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
