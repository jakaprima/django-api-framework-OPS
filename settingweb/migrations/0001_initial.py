# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-23 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SettingWeb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_web', models.CharField(max_length=35)),
                ('deskripsi_web', models.CharField(max_length=60)),
            ],
        ),
    ]
