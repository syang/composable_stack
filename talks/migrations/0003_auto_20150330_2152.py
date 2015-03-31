# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0002_auto_20150330_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='speaker_rating',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='talk',
            name='talk_rating',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=True,
        ),
    ]
