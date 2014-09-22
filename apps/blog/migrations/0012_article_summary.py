# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20140922_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.TextField(default=datetime.date(2014, 9, 22), verbose_name='Summary'),
            preserve_default=False,
        ),
    ]
