# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20140922_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title_image',
            field=models.ImageField(upload_to=b'thumbnail', null=True, verbose_name='\u56fe\u7247', blank=True),
        ),
    ]
