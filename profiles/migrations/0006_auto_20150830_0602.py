# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_researcher_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researcher',
            name='pic',
            field=sorl.thumbnail.fields.ImageField(default=b'static/img/eintein.jpg', upload_to=b'researcher_images'),
        ),
    ]
