# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(
                    max_length=100, verbose_name='Title')),
                ('tags', models.CharField(help_text="Use the comma(',') separated",
                                          max_length=100, null=True, verbose_name='Tags', blank=True)),
                ('content', models.TextField(verbose_name='Content')),
                ('status', models.IntegerField(default=0, verbose_name='Status', choices=[
                 (0, 'Publish'), (1, 'Draft'), (2, 'Delete')])),
                ('view_times', models.IntegerField(default=1)),
                ('is_top', models.BooleanField(
                    default=False, verbose_name='Top')),
                ('create_time', models.DateTimeField(
                    auto_now_add=True, verbose_name='Create Time')),
                ('update_time', models.DateTimeField(
                    auto_now=True, verbose_name='Update Time')),
                ('author', models.ForeignKey(
                    verbose_name='Author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-is_top', '-update_time', '-create_time'],
                'verbose_name': 'Article',
                'verbose_name_plural': 'Article',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('desc', models.CharField(help_text='Description of a category.',
                                          max_length=100, verbose_name='Description', blank=True)),
                ('is_nav', models.BooleanField(
                    default=False, verbose_name='Display on the navbar.')),
                ('rank', models.IntegerField(
                    default=0, verbose_name='Display order.')),
                ('status', models.IntegerField(default=0, verbose_name='Status', choices=[
                 (0, 'Publish'), (1, 'Draft'), (2, 'Delete')])),
                ('create_time', models.DateTimeField(
                    auto_now_add=True, verbose_name='Create Time')),
                ('update_time', models.DateTimeField(
                    auto_now=True, verbose_name='Update Time')),
                ('parent', models.ForeignKey(default=None, blank=True,
                                             to='blog.Category', null=True, verbose_name='Parent category.')),
            ],
            options={
                'ordering': ['rank', '-create_time'],
                'verbose_name': 'Category',
                'verbose_name_plural': 'Category',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(
                verbose_name='\u5206\u7c7b', to='blog.Category'),
            preserve_default=True,
        ),
    ]
