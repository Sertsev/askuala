# Generated by Django 4.1.1 on 2022-09-30 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_users', '0009_alter_guests_options_alter_lecturers_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrars',
            name='EducationLevel',
        ),
        migrations.AddField(
            model_name='registrars',
            name='educationDepartment',
            field=models.CharField(choices=[('Computer Science', 'Computer Science'), ('Business Administration', 'Business Administration')], default='Business Adminstration', max_length=127),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrars',
            name='educationLevel',
            field=models.CharField(choices=[('MA', 'MA'), ('MS', 'MS'), ('BSc', 'BSc'), ('BA', 'BA'), ('BEng', 'BEng')], default='Bachelor', max_length=127),
        ),
    ]
