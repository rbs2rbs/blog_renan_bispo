# Generated by Django 3.0.4 on 2020-03-30 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20200330_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='educacao',
            name='local',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
