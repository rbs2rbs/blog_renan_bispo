# Generated by Django 3.0.4 on 2020-03-31 12:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20200331_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='data_criado',
            field=models.DateField(default=datetime.datetime(2020, 3, 31, 12, 3, 4, 263042, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
