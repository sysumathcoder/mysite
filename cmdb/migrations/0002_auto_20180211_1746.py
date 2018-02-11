# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='pwd',
            new_name='change',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='user',
            new_name='name',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='price',
            field=models.CharField(default=datetime.datetime(2018, 2, 11, 17, 45, 46, 205990, tzinfo=utc), max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='time',
            field=models.CharField(default=datetime.datetime(2018, 2, 11, 17, 46, 11, 750570, tzinfo=utc), max_length=32),
            preserve_default=False,
        ),
    ]
