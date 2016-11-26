# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-26 16:07
from __future__ import unicode_literals

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='blog_image'),
        ),
    ]
