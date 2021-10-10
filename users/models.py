from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import BLANK_CHOICE_DASH, NullBooleanField
from django.utils.formats import date_format
import os

def path_and_rename(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    if instance.user.username:
        filename = 'User_Profile_Pictures/{}.{}'.format(instance.user.username, ext)
    return os.path.join(upload_to, filename)

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    firstname = models.CharField(max_length=64)
    middlename = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    phonenumber = models.CharField(max_length=32)
    # username = models.CharField(max_length=64)
    # password1 = models.CharField(max_length=128)
    # password2 = models.CharField(max_length=128)

    profile_pic = models.ImageField(upload_to=path_and_rename, verbose_name="Profile Pictures", blank=True)

    student = 'Student'
    teacher = 'Teacher'
    registrar = 'Registrar'
    guest = 'Guest'

    user_types = [
        (student, 'Student'),
        (teacher, 'Teacher'),
        (registrar, 'Registrar'),
        (guest, 'Guest')
    ]

    user_type = models.CharField(max_length=15, choices=user_types, default=BLANK_CHOICE_DASH)

    bsc = 'BSc'
    ba = 'BA'
    ms = 'MS'
    ma = 'MBA'
    programs = [
        (bsc, 'BSc'),
        (ba, 'BA'),
        (ms, 'MS'),
        (ma, 'MBA'),
    ]

    program = models.CharField(max_length=10, choices=programs, blank=True)

    computerScience = 'Computer Science'
    businessAdmin = 'Business Administration'
    
    Departments = [
        (computerScience, 'Computer Science'),
        (businessAdmin, 'Business Administration')
    ]
    
    department = models.CharField(max_length=50, choices=Departments, blank=True)

    def __str__(self):
        return self.user.username
