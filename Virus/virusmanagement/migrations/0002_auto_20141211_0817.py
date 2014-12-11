# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('virusmanagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='handlelog',
            name='op_time',
            field=models.DateField(default=datetime.date(2014, 12, 11)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viruslog',
            name='is_handled',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
