# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_article_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=models.TextField(verbose_name='Summary', validators=[django.core.validators.MinLengthValidator(8)]),
        ),
    ]
