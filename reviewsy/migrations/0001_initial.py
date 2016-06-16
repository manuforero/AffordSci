# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 22:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('summary', models.CharField(max_length=240)),
                ('body', models.TextField()),
                ('duration', models.DurationField()),
            ],
        ),
    ]
