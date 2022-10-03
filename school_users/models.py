from enum import unique
import os
from datetime import datetime
from django.db import models
from programs.models import Course, Department, Batch, Program

""" More info when filtering techniques rewatch 42 - 53 """

def path_and_rename(instance, filename):
    upload_to = 'Images/'
    # ext = filename.split('.')[-1]
    # if instance.user.username:
    #     filename = 'User_Profile_Pictures/{}.{}'.format(instance.user.username, ext)
    return os.path.join(upload_to, filename)


class Registrar(models.Model):
    registrarId = models.AutoField(primary_key=True, verbose_name="ID")
    firstName = models.CharField(max_length=63, verbose_name="First Name")
    middleName = models.CharField(max_length=63, verbose_name="Middle Name")
    lastName = models.CharField(max_length=63, verbose_name="Last Name")
    Gender = [
        ('M', "Male"),
        ('F', "Female"),
    ]
    gender = models.CharField(max_length=1, choices=Gender)

    email = models.EmailField(max_length=63, unique=True)
    password = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=32, null=True, verbose_name="Phone Number")
    birthdate = models.DateField(null=True)

    profilePicDir = models.ImageField(upload_to=path_and_rename, verbose_name="Profile Photo Directory", blank=True)
    educationLevel = models.CharField(max_length=127, default='Bachelor', choices=[(x, x) for x in [a.programName for a in Program.objects.all()]], verbose_name="Education Level")
    educationDepartment = models.CharField(max_length=127, choices=[(x, x) for x in [a.departmentName for a in Department.objects.all()]], verbose_name="Department")

    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="Account Creation Date")
    lastUpdate = models.DateField(auto_now=True, verbose_name="Last Update")
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.firstName

    def full_name(self):
        return self.firstName + ' ' + self.middleName + ' ' + self.lastName

    class Meta:
        ordering = ['firstName', 'middleName', 'lastName']

class Student(models.Model):
    studentId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=63, verbose_name="First Name")
    middleName = models.CharField(max_length=63, verbose_name="Middle Name")
    lastName = models.CharField(max_length=63, verbose_name="Last Name")
    Gender = [
        ('M', "Male"),
        ('F', "Female"),
    ]
    gender = models.CharField(max_length=1, choices=Gender)

    email = models.EmailField(max_length=63, unique=True)
    password = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=32, null=True, verbose_name="Phone Number")
    birthdate = models.DateField(null=True)
    citizenship = models.CharField(max_length=127, null=True)
    country = models.CharField(max_length=127, null=True)
    city = models.CharField(max_length=63, null=True)

    documentLocation = models.CharField(max_length=511, null=True, verbose_name="Documents Location")
    profilePicDir = models.ImageField(upload_to=path_and_rename, verbose_name="Profile Photo Directory", blank=True)
    previousEducationLevel = models.CharField(max_length=127, choices=[(x, x) for x in [a.programName for a in Program.objects.all()]], verbose_name="Previous Education Level")
    previousEducationDepartment = models.CharField(max_length=127, choices=[(x, x) for x in [a.departmentName for a in Department.objects.all()]], verbose_name="Previous Study")
    # shortCourses = models.ManyToManyField(Courses)

    Years = [(r,r) for r in range(2020, datetime.now().year + 1)]
    academicYear = models.PositiveSmallIntegerField(choices=Years, default=2022, verbose_name="Academic Year")

    currentSemester = models.PositiveSmallIntegerField(choices=[(1,1), (2,2)], verbose_name="Current Semester")
    program = models.ForeignKey(Program, null=True, on_delete=models.SET_NULL)
    department = models.ManyToManyField(Department)
    courses = models.ManyToManyField(Course)
    batch = models.ForeignKey(Batch, null=True, on_delete=models.SET_NULL)
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="Account Creation Date")
    lastUpdate = models.DateField(auto_now=True, verbose_name="Last Update")
    verified = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    enrollments = [
        ("Regular", "Regular"),
        ("Online","Online")
    ]
    enrollment_type = models.CharField(max_length=23, choices=enrollments, default="Regular", verbose_name="Enrollment")

    def __str__(self):
        return self.firstName
    
    def full_name(self):
        return self.firstName + ' ' + self.middleName + ' ' + self.lastName

    class Meta:
        ordering = ['firstName', 'middleName', 'lastName']


class Lecturer(models.Model):
    lectureId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=63, verbose_name="First Name")
    middleName = models.CharField(max_length=63, verbose_name="Middle Name")
    lastName = models.CharField(max_length=63, verbose_name="Last Name")
    Gender = [
        ('M', "Male"),
        ('F', "Female"),
    ]
    gender = models.CharField(max_length=1, choices=Gender)

    email = models.EmailField(max_length=63, unique=True)
    password = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=32, null=True, verbose_name="Phone Number")
    birthdate = models.DateField(null=True)
    citizenship = models.CharField(max_length=127, null=True)
    country = models.CharField(max_length=127, null=True)
    city = models.CharField(max_length=63, null=True)

    documentLocation = models.CharField(max_length=511, null=True, verbose_name="Documents Location")
    profilePicDir = models.ImageField(upload_to=path_and_rename, verbose_name="Profile Photo Directory", blank=True)
    educationLevel = models.CharField(max_length=127, default='Bachelor', choices=[(x, x) for x in [a.programName for a in Program.objects.all()]], verbose_name="Education Level")
    educationDepartment = models.CharField(max_length=127, choices=[(x, x) for x in [a.departmentName for a in Department.objects.all()]], verbose_name="Department")

    program = models.ManyToManyField(Program)
    department = models.ManyToManyField(Department)
    courses = models.ManyToManyField(Course)
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="Account Creation Date")
    lastUpdate = models.DateField(auto_now=True, verbose_name="Last Update")
    verified = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.firstName

    def full_name(self):
        return self.firstName + ' ' + self.middleName + ' ' + self.lastName

    class Meta:
        ordering = ['firstName', 'middleName', 'lastName']

class Guest(models.Model):
    guestId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=63, verbose_name="First Name")
    middleName = models.CharField(max_length=63, verbose_name="Middle Name")
    lastName = models.CharField(max_length=63, verbose_name="Last Name")
    Gender = [
        ('M', "Male"),
        ('F', "Female"),
    ]
    gender = models.CharField(max_length=1, choices=Gender)

    email = models.EmailField(max_length=63, unique=True)
    password = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=32, null=True, verbose_name="Phone Number")
    birthdate = models.DateField(null=True)
    citizenship = models.CharField(max_length=127, default='Ethiopian' ,null=True)
    country = models.CharField(max_length=127, default='Ethiopia', null=True)
    city = models.CharField(max_length=63, default='Addis Ababa', null=True)

    documentLocation = models.CharField(max_length=511, null=True, verbose_name="Documents Location")
    profilePicDir = models.ImageField(upload_to=path_and_rename, verbose_name="Profile Photo Directory", blank=True)
    educationLevel = models.CharField(max_length=127, default='Bachelor', choices=[(x, x) for x in [a.programName for a in Program.objects.all()]], verbose_name="Education Level")
    educationDepartment = models.CharField(max_length=127, choices=[(x, x) for x in [a.departmentName for a in Department.objects.all()]], verbose_name="Previous Study")
    shortCourses = models.ManyToManyField(Course)

    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="Account Creation Date")
    lastUpdate = models.DateField(auto_now=True, verbose_name="Last Update")
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.firstName

    def full_name(self):
        return self.firstName + ' ' + self.middleName + ' ' + self.lastName

    class Meta:
        ordering = ['firstName', 'middleName', 'lastName']
