# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wmd.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(verbose_name='Category', to='blog.Category'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=wmd.models.MarkDownField(verbose_name='Content'),
        ),
    ]
