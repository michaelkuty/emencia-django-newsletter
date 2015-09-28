# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='smtpserver',
            name='ssl',
            field=models.BooleanField(default=True, verbose_name='server use SSL'),
        ),
    ]
