import os
from django.db import models
from programs.models import Course, Department, Batch, Program
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

""" More info when filtering techniques re-watch 42 - 53 """

def path_and_rename(instance, filename):
    upload_to = 'Images/'
    # ext = filename.split('.')[-1]
    # if instance.user.username:
    #     filename = 'User_Profile_Pictures/{}.{}'.format(instance.user.username, ext)
    return os.path.join(upload_to, filename)


class User(AbstractUser):
    middle_name = models.CharField(_("Middle Name"), max_length=150, blank=True)
    email = models.EmailField(max_length=63, unique=True)
    Gender = [
        ('M', "Male"),
        ('F', "Female"),
    ]
    gender = models.CharField(max_length=1, choices=Gender)
    phone_number = models.CharField(_("Phone Number"), max_length=32, unique=True)
    user_type = models.CharField(max_length=23, default='guest',
                choices=[("guest", "guest"), 
                        ("student", "student"), 
                        ("lecturer", "lecturer"), 
                        ("registrar", "registrar")
                        ])


class Guest(models.Model):
    guestId = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    birthdate = models.DateField(null=True, blank=True)

    """
        A user physical location
    """
    citizenship = models.CharField(max_length=127, null=True, blank=True)
    currentCountry = models.CharField(max_length=127, null=True, blank=True)
    city = models.CharField(max_length=63, null=True, blank=True)
    address = models.CharField(max_length=127, blank=True, null=True)

    """
        A list of degree programs available in the world
    """
    progs = [
        ('Bachelor of Arts', "BA"),
        ('Bachelor of Business Administration', "BBA"),
        ('Bachelor of Fine Arts', "BFA"),
        ('Bachelor of Science', "BS"),
        ('Bachelor of Engineering', "B.Eng."),
        ('Master of Science', "MS"),
        ('Master of Arts', "MA"),
        ('Master of Business Administration', "MBA"),
        ('Doctor of philosophy', "Ph.D."),
        ('Other', 'Other')
    ]
    educationLevel = models.CharField(
        max_length=127, default='Bachelor', choices=progs, verbose_name="Education Level")

    """
        A list of degree departments available in the world
    """
    deps = [
        ('Theatrical Science', "Theatrical Science"),
        ('Business Administration', "Business Administration"),
        ('Health Informatics', "Health Informatics"),
        ('Public Health', "Public Health"),
        ('Electrical Engineering', "Electrical Engineering"),
        ('Computer Science', "Computer Science"),
        ('Accounting', "Accounting"),
        ('Marketing Management', "Marketing Management"),
        ('Software Engineering', "Software Engineering"),
        ('Other', 'Other')
    ]
    educationDepartment = models.CharField(
        max_length=127, choices=deps, verbose_name="Department")

    """
        The user documents location on the server
    """
    profilePicDir = models.ImageField(
        upload_to=path_and_rename, null=True, verbose_name="Profile Photo Directory", blank=True)
    documentLocation = models.CharField(
        max_length=511, null=True, verbose_name="Documents Location", blank=True)

    """
        Time stamps of the registered object
    """
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="Account Creation Date", blank=True)
    lastUpdate = models.DateTimeField(
        auto_now=True, verbose_name="Last Update", blank=True)

    def __str__(self):
        return self.user.username

    def full_name(self):
        return self.user.first_name + ' ' + self.user.middle_name + ' ' + self.user.last_name

    class Meta:
        ordering = ['user__first_name', 'user__middle_name', 'user__last_name']


class Registrar(models.Model):
    registrarId = models.AutoField(primary_key=True, verbose_name="ID")
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    birthdate = models.DateField(null=True, blank=True)

    """
        A user physical location
    """
    citizenship = models.CharField(max_length=127, null=True, blank=True)
    currentCountry = models.CharField(max_length=127, null=True, blank=True)
    city = models.CharField(max_length=63, null=True, blank=True)
    address = models.CharField(max_length=127, blank=True, null=True)

    """
        A list of degree programs available in the world
    """
    progs = [
        ('Bachelor of Arts', "BA"),
        ('Bachelor of Business Administration', "BBA"),
        ('Bachelor of Fine Arts', "BFA"),
        ('Bachelor of Science', "BS"),
        ('Bachelor of Engineering', "B.Eng."),
        ('Master of Science', "MS"),
        ('Master of Arts', "MA"),
        ('Master of Business Administration', "MBA"),
        ('Doctor of philosophy', "Ph.D."),
        ('Other', 'Other')
    ]
    educationLevel = models.CharField(
        max_length=127, default='Bachelor', choices=progs, verbose_name="Education Level")

    """
        A list of degree departments available in the world
    """
    deps = [
        ('Theatrical Science', "Theatrical Science"),
        ('Business Administration', "Business Administration"),
        ('Health Informatics', "Health Informatics"),
        ('Public Health', "Public Health"),
        ('Electrical Engineering', "Electrical Engineering"),
        ('Computer Science', "Computer Science"),
        ('Accounting', "Accounting"),
        ('Marketing Management', "Marketing Management"),
        ('Software Engineering', "Software Engineering"),
        ('Other', 'Other')
    ]
    educationDepartment = models.CharField(
        max_length=127, choices=deps, verbose_name="Department")

    """
        The user documents location on the server
    """
    # profilePicDir = models.ImageField(
    #     # upload_to=path_and_rename, null=True, verbose_name="Profile Photo Directory", blank=True)
    documentLocation = models.CharField(
        max_length=511, null=True, verbose_name="Documents Location", blank=True)
    
    """
        Time stamps of the registered object
    """
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="Account Creation Date", blank=True)
    lastUpdate = models.DateTimeField(
        auto_now=True, verbose_name="Last Update", blank=True)

    def __str__(self):
        return self.user.username

    def full_name(self):
        return self.user.first_name + ' ' + self.user.middle_name + ' ' + self.user.last_name

    class Meta:
        ordering = ['user__first_name', 'user__middle_name', 'user__last_name']


class Student(models.Model):
    studentId=models.AutoField(primary_key=True, verbose_name="ID")
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    birthdate = models.DateField(null=True, blank=True)

    """
        A user physical location
    """
    citizenship = models.CharField(max_length=127, null=True, blank=True)
    currentCountry = models.CharField(max_length=127, null=True, blank=True)
    city = models.CharField(max_length=63, null=True, blank=True)
    address = models.CharField(max_length=127, blank=True, null=True)

    """
        A list of degree programs available in the world
    """
    progs = [
        ('Bachelor of Arts', "BA"),
        ('Bachelor of Business Administration', "BBA"),
        ('Bachelor of Fine Arts', "BFA"),
        ('Bachelor of Science', "BS"),
        ('Bachelor of Engineering', "B.Eng."),
        ('Master of Science', "MS"),
        ('Master of Arts', "MA"),
        ('Master of Business Administration', "MBA"),
        ('Doctor of philosophy', "Ph.D."),
        ('Other', 'Other')
    ]
    educationLevel = models.CharField(
        max_length=127, default='Bachelor', choices=progs, verbose_name="Education Level")

    """
        A list of degree departments available in the world
    """
    deps = [
        ('Theatrical Science', "Theatrical Science"),
        ('Business Administration', "Business Administration"),
        ('Health Informatics', "Health Informatics"),
        ('Public Health', "Public Health"),
        ('Electrical Engineering', "Electrical Engineering"),
        ('Computer Science', "Computer Science"),
        ('Accounting', "Accounting"),
        ('Marketing Management', "Marketing Management"),
        ('Software Engineering', "Software Engineering"),
        ('Other', 'Other')
    ]
    educationDepartment = models.CharField(
        max_length=127, choices=deps, verbose_name="Department")

    """
        The user documents location on the server
    """
    # profilePicDir = models.ImageField(
    #     upload_to=path_and_rename, null=True, verbose_name="Profile Photo Directory", blank=True)
    documentLocation = models.CharField(
        max_length=511, null=True, verbose_name="Documents Location", blank=True)

    currentYear = models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=2022, verbose_name="Academic Year")
    currentSemester = models.PositiveSmallIntegerField(choices=[(1,1), (2,2)], verbose_name="Current Semester")
    enrolledProgram = models.ForeignKey(Program, on_delete=models.PROTECT)
    enrolledDepartment = models.ForeignKey(Department, on_delete=models.PROTECT)
    batch = models.ForeignKey(Batch, on_delete=models.PROTECT)

    """
        Time stamps of the registered object
    """
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Account Creation Date", blank=True)
    lastUpdate = models.DateTimeField(
        auto_now=True, verbose_name="Last Update", blank=True)

    enrollments = [
        ("Regular", "Regular"),
        ("Online", "Online")
    ]
    enrollment_type = models.CharField(
        max_length=23, choices=enrollments, default="Regular", verbose_name="Enrollment")

    def __str__(self):
        return self.user.username
    
    def full_name(self):
        return self.user.first_name + ' ' + self.user.middle_name + ' ' + self.user.last_name

    class Meta:
        ordering = ['user__first_name', 'user__middle_name', 'user__last_name']


class Lecturer(models.Model):
    lecturerId = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    birthdate = models.DateField(null=True, blank=True)

    """
        A user physical location
    """
    citizenship = models.CharField(max_length=127, null=True, blank=True)
    currentCountry = models.CharField(max_length=127, null=True, blank=True)
    city = models.CharField(max_length=63, null=True, blank=True)
    address = models.CharField(max_length=127, blank=True, null=True)

    """
        A list of degree programs available in the world
    """
    progs = [
        ('Bachelor of Arts', "BA"),
        ('Bachelor of Business Administration', "BBA"),
        ('Bachelor of Fine Arts', "BFA"),
        ('Bachelor of Science', "BS"),
        ('Bachelor of Engineering', "B.Eng."),
        ('Master of Science', "MS"),
        ('Master of Arts', "MA"),
        ('Master of Business Administration', "MBA"),
        ('Doctor of philosophy', "Ph.D."),
        ('Other', 'Other')
    ]
    educationLevel = models.CharField(
        max_length=127, default='Bachelor', choices=progs, verbose_name="Education Level")

    """
        A list of degree departments available in the world
    """
    deps = [
        ('Theatrical Science', "Theatrical Science"),
        ('Business Administration', "Business Administration"),
        ('Health Informatics', "Health Informatics"),
        ('Public Health', "Public Health"),
        ('Electrical Engineering', "Electrical Engineering"),
        ('Computer Science', "Computer Science"),
        ('Accounting', "Accounting"),
        ('Marketing Management', "Marketing Management"),
        ('Software Engineering', "Software Engineering"),
        ('Other', 'Other')
    ]
    educationDepartment = models.CharField(
        max_length=127, choices=deps, verbose_name="Department")

    """
        The user documents location on the server
    """
    # profilePicDir = models.ImageField(
    #     upload_to=path_and_rename, null=True, verbose_name="Profile Photo Directory", blank=True)
    documentLocation = models.CharField(
        max_length=511, null=True, verbose_name="Documents Location", blank=True)

    """
        Time stamps of the registered object
    """
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Account Creation Date", blank=True)
    lastUpdate = models.DateTimeField(
        auto_now=True, verbose_name="Last Update", blank=True)

    def __str__(self):
        return self.user.username

    def full_name(self):
        return self.user.first_name + ' ' + self.user.middle_name + ' ' + self.user.last_name

    class Meta:
        ordering = ['user__first_name', 'user__middle_name', 'user__last_name']


class AssignCourses(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.PROTECT)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    registrar = models.ForeignKey(Registrar, on_delete=models.DO_NOTHING)
    course_type = models.CharField(max_length=127, choices=[('Short Courses', 'Short Courses'), ('Courses', 'Course')], default='Courses')
    """
        Time stamps of the registered object
    """
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Account Creation Date", blank=True)
    lastUpdate = models.DateTimeField(auto_now=True, verbose_name="Last Update", blank=True)
