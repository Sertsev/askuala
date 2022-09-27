import os
from datetime import datetime
from django.db import models
from programs.models import Courses, Department, Program, Batches

def path_and_rename(instance, filename):
    upload_to = 'Images/'
    # ext = filename.split('.')[-1]
    # if instance.user.username:
    #     filename = 'User_Profile_Pictures/{}.{}'.format(instance.user.username, ext)
    return os.path.join(upload_to, filename)


class Registrars(models.Model):
    registrarId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=63)
    middleName = models.CharField(max_length=63)
    lastName = models.CharField(max_length=63)
    Gender = [
        ('M', "Male"),
        ('F', "Female"),
    ]
    gender = models.CharField(max_length=1, choices=Gender)

    email = models.EmailField(max_length=63, null=True)
    password = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=32, null=True)
    birthdate = models.DateField(null=True)

    profilePicDir = models.ImageField(upload_to=path_and_rename, verbose_name="Profile Pictures", blank=True)
    EducationLevel = models.ForeignKey(Program, null=True, on_delete=models.SET_NULL)

    createdAt = models.DateTimeField(auto_now_add=True)
    lastUpdate = models.DateField(auto_now=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.firstName


class Students(models.Model):
    studentId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=63)
    middleName = models.CharField(max_length=63)
    lastName = models.CharField(max_length=63)

    Gender = [
        ('M', "Male"),
        ('F', "Female"),
    ]
    gender = models.CharField(max_length=1, choices=Gender)

    email = models.EmailField(max_length=63, null=True)
    password = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=32, null=True)
    birthdate = models.DateField(null=True)
    citizenship = models.CharField(max_length=127, null=True)
    country = models.CharField(max_length=127, null=True)
    city = models.CharField(max_length=63, null=True)

    documentLocation = models.CharField(max_length=511, null=True)
    profilePicDir = models.ImageField(upload_to=path_and_rename, verbose_name="Profile Pictures", blank=True)
    previousEducationLevel = models.CharField(max_length=127, default='Bachelor', choices=[(x, x) for x in [a.programName for a in Program.objects.all()]])

    Years = [(r,r) for r in range(2020, datetime.now().year + 1)]
    academicYear = models.PositiveSmallIntegerField(choices=Years, default=2022)

    currentSemester = models.PositiveSmallIntegerField(choices=[(1,1), (2,2)])
    program = models.ForeignKey(Program, null=True, on_delete=models.SET_NULL)
    department = models.ManyToManyField(Department)
    courses = models.ManyToManyField(Courses)
    batch = models.ForeignKey(Batches, null=True, on_delete=models.SET_NULL)
    createdAt = models.DateTimeField(auto_now_add=True)
    lastUpdate = models.DateTimeField(auto_now=True)
    verified = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    enrollments = [
        ("Regular", "Regular"),
        ("Online","Online")
    ]
    enrollment_type = models.CharField(max_length=23, choices=enrollments, default="Regular")

    def __str__(self):
        return self.firstName


class Lecturers(models.Model):
    lectureId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=63)
    middleName = models.CharField(max_length=63)
    lastName = models.CharField(max_length=63)

    Gender = [
        ('M', "Male"),
        ('F', "Female"),
    ]
    gender = models.CharField(max_length=1, choices=Gender)

    email = models.EmailField(max_length=63, null=True)
    password = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=32, null=True)
    birthdate = models.DateField(null=True)
    citizenship = models.CharField(max_length=127, null=True)
    country = models.CharField(max_length=127, null=True)
    city = models.CharField(max_length=63, null=True)

    documentLocation = models.CharField(max_length=511, null=True)
    profilePicDir = models.ImageField(upload_to=path_and_rename, verbose_name="Profile Pictures", blank=True)
    EducationLevel = models.CharField(max_length=255)

    program = models.ManyToManyField(Program)
    department = models.ManyToManyField(Department)
    courses = models.ManyToManyField(Courses)
    createdAt = models.DateTimeField(auto_now_add=True)
    lastUpdate = models.DateField(auto_now=True)
    verified = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.firstName


class Guests(models.Model):
    guestId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=63)
    middleName = models.CharField(max_length=63)
    lastName = models.CharField(max_length=63)

    Gender = [
        ('M', "Male"),
        ('F', "Female"),
    ]
    gender = models.CharField(max_length=1, choices=Gender)

    email = models.EmailField(max_length=63, null=True)
    password = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=32, null=True)
    birthdate = models.DateField(null=True)
    citizenship = models.CharField(max_length=127, default='Ethiopian' ,null=True)
    country = models.CharField(max_length=127, default='Ethiopia', null=True)
    city = models.CharField(max_length=63, default='Addis Ababa', null=True)

    documentLocation = models.CharField(max_length=511, null=True)
    profilePicDir = models.ImageField(upload_to=path_and_rename, verbose_name="Profile Pictures", blank=True)
    EducationLevel = models.CharField(max_length=255)
    courses = models.ManyToManyField(Courses)

    createdAt = models.DateTimeField(auto_now_add=True)
    lastUpdate = models.DateField(auto_now=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.firstName