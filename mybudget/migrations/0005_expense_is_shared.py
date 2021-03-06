# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mybudget', '0004_auto_20141118_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='is_shared',
            field=models.BooleanField(default=False, verbose_name='Is shared'),
            preserve_default=True,
        ),
    ]
