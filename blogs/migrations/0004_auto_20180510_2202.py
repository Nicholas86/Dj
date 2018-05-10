# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-10 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20180503_1734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='description',
            new_name='content',
        ),
        migrations.AddField(
            model_name='blog',
            name='char_num',
            field=models.IntegerField(default=0, verbose_name='字数统计'),
        ),
    ]