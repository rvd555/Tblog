# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20140922_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title_image',
            field=imagekit.models.fields.ProcessedImageField(upload_to=b'thumbnail'),
        ),
    ]
