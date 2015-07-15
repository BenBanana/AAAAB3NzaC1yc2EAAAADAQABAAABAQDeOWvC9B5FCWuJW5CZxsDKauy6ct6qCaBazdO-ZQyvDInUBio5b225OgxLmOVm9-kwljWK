# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('month', models.CharField(default=b' ', max_length=30, choices=[(b'January', b'January'), (b'February', b'February'), (b'March', b'March'), (b'April', b'April'), (b'May', b'May'), (b'June', b'June'), (b'July', b'July'), (b'August', b'August'), (b'September', b'September'), (b'October', b'October'), (b'November', b'November'), (b'December', b'December'), (b' ', b'--')])),
                ('day', models.CharField(max_length=2)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
