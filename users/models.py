from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)

    batch = models.IntegerField(default=1)

    profile_pic = models.ImageField(upload_to='Images', verbose_name="Profile Pictures",blank=True)

    computerScience = 'Computer Science'
    businessAdmin = 'Business Administration'
    
    Departments = [
        (computerScience, 'Computer Science'),
        (businessAdmin, 'Business Administration')
    ]
    
    department = models.CharField(max_length=50, choices=Departments, default=computerScience)

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

    user_type = models.CharField(max_length=15, choices=user_types, default=student)

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

    program = models.CharField(max_length=10, choices=programs, default=ms)

    def __str__(self):
        return self.user.username