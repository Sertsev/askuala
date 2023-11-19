# Generated by Django 3.2.7 on 2021-10-07 21:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=64)),
                ('middlename', models.CharField(max_length=64)),
                ('lastname', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=64)),
                ('phonenumber', models.CharField(max_length=32)),
                ('profile_pic', models.ImageField(blank=True, upload_to=users.models.path_and_rename, verbose_name='Profile Pictures')),
                ('user_type', models.CharField(choices=[('Student', 'Student'), ('Teacher', 'Teacher'), ('Registrar', 'Registrar'), ('Guest', 'Guest')], default='Student', max_length=15)),
                ('program', models.CharField(choices=[('BSc', 'BSc'), ('BA', 'BA'), ('MS', 'MS'), ('MBA', 'MBA')], default='MS', max_length=10)),
                ('department', models.CharField(choices=[('Computer Science', 'Computer Science'), ('Business Administration', 'Business Administration')], default='Computer Science', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]