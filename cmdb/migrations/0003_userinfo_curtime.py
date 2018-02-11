# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0002_auto_20180211_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='curTime',
            field=models.CharField(max_length=32, default=1),
            preserve_default=False,
        ),
    ]
