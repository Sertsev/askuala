# Generated by Django 4.1.1 on 2022-09-28 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0008_remove_program_programinfolink'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='programInfoLink',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='program',
            name='resourceAddress',
            field=models.CharField(max_length=127, null=True),
        ),
    ]
