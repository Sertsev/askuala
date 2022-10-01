# Generated by Django 4.1.1 on 2022-10-01 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0010_rename_batches_batch_rename_courses_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses_in_batch',
            name='program',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='programs.program'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='department',
            name='program',
        ),
        migrations.AddField(
            model_name='department',
            name='program',
            field=models.ManyToManyField(to='programs.program'),
        ),
    ]
