# Generated by Django 4.1.1 on 2022-10-01 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_users', '0011_guest_lecturer_registrar_student_and_more'),
        ('programs', '0009_program_programinfolink_program_resourceaddress'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Batches',
            new_name='Batch',
        ),
        migrations.RenameModel(
            old_name='Courses',
            new_name='Course',
        ),
    ]
