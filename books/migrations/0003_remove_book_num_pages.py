# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20150726_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='num_pages',
        ),
    ]
