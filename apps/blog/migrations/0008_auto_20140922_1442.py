# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20140922_1439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='title_image',
        ),
        migrations.AddField(
            model_name='article',
            name='title_image',
            field=models.FileField(upload_to=b'thumbnail', null=True, verbose_name='\u56fe\u7247', blank=True),
            preserve_default=True,
        ),
    ]
