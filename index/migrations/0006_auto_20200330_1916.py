# Generated by Django 3.0.4 on 2020-03-30 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20200330_1853'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Habilidades',
            new_name='Habilidade',
        ),
        migrations.AddField(
            model_name='experiencia',
            name='local',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
