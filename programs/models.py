from django.conf import settings
from datetime import datetime, date
from django.db import models
from askuala.settings import AUTH_USER_MODEL

class Batch(models.Model):
    batchId = models.AutoField(primary_key=True)
    batchName = models.CharField(max_length=63, verbose_name="Batch Name")
    batchProgram = models.CharField(max_length=23, choices=[('Master', 'Master'), ('Bachelor', 'Bachelor')], verbose_name="Batch Program")
    Years = [(r,r) for r in range(2020, datetime.now().year + 1)]
    batchEntryYear = models.PositiveSmallIntegerField(choices=Years, default=date.today().year, verbose_name="Entry Year")
    batchGraduationYear = models.DateField(verbose_name="Graduation Year")
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="Creation TimeStamp", blank=True)
    lastUpdate = models.DateTimeField(
        auto_now=True, verbose_name="Last Update", blank=True)

    def __str__(self):
        return self.batchName

    class Meta:
        ordering = ['batchName']


class Program(models.Model):
    programId = models.AutoField(primary_key=True)
    programName = models.CharField(max_length=63, verbose_name="Program Name")
    programDescription = models.CharField(max_length=63, null=True, verbose_name="Title", blank=True)
    programInfoLink = models.CharField(max_length=255, default='Not set', verbose_name="More Information Link", blank=True)
    resourceAddress = models.CharField(max_length=127, null=True, verbose_name="Resource Address", blank=True)
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Creation TimeStamp", blank=True)
    lastUpdate = models.DateTimeField(auto_now=True, verbose_name="Last Update", blank=True)

    def __str__(self):
        return self.programName


class Department(models.Model):
    departmentId = models.AutoField(primary_key=True)
    departmentName = models.CharField(max_length=127, verbose_name="Department Name")
    departmentDescription = models.TextField(null=True, verbose_name="Description", blank=True)
    departmentInfoLink = models.CharField(
        max_length=255, default='Not set', verbose_name="More Information Link", blank=True)
    program = models.ManyToManyField(Program)
    departmentHead = models.CharField(max_length=127, null=True, blank=True, verbose_name="Department Head")
    # departmentHead = models.ForeignKey('school_users.Lecturer', on_delete=models.PROTECT)
    resources = models.CharField(max_length=127, null=True, blank=True)
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Creation TimeStamp", blank=True)
    lastUpdate = models.DateTimeField(auto_now=True, verbose_name="Last Update", blank=True)
    

    def __str__(self):
        return self.departmentName


class Course(models.Model):
    courseId = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=255, verbose_name="Course Name")
    courseDescription = models.TextField(null=True, verbose_name="Description", blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    resources = models.CharField(max_length=127, null=True, blank=True)
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Creation TimeStamp", blank=True)
    lastUpdate = models.DateTimeField(auto_now=True, verbose_name="Last Update", blank=True)
    
    def __str__(self):
        return self.courseName

    def departmentName(self):
        return self.department.departmentName 


class Courses_in_Batch(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    year = models.PositiveSmallIntegerField(
        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    semester = models.PositiveSmallIntegerField(choices=[(1,1), (2,2)])
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    courseStarts = models.DateField(null=True)
    endCourse = models.DateField(null=True)
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Creation TimeStamp", blank=True)
    lastUpdate = models.DateTimeField(
        auto_now=True, verbose_name="Last Update", blank=True)

    def __str__(self):
        return self.batch.batchName + " " + self.program.programName

    def programName(self):
        return self.program.programName

    def courseName(self):
        return self.course.courseName
    
    def departmentName(self):
        return self.department.departmentName

    class Meta:
        verbose_name = "Courses in batch"


class Lesson(models.Model):
    lessonTitle = models.CharField(max_length=255, verbose_name="Lesson Title")
    lessonDescription = models.TextField(
        null=True, verbose_name="Description", blank=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    lecturer = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT) 
    resources = models.CharField(max_length=127, null=True, blank=True)
    embedVideo = models.CharField(max_length=127, null=True, blank=True)
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Creation TimeStamp", blank=True)
    lastUpdate = models.DateTimeField(
        auto_now=True, verbose_name="Last Update", blank=True)


# handling enrollment applications
class StudentApplications(models.Model):
    applicationId = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True)
    guest = models.OneToOneField(
        settings.GUEST_USER_MODEL, on_delete=models.CASCADE, unique=True)
    program = models.ForeignKey(Program, on_delete=models.PROTECT)
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT)
    batch = models.ForeignKey(Batch, on_delete=models.PROTECT)
    enrollments = [
        ("Regular", "Regular"),
        ("Online", "Online")
    ]
    enrollment_type = models.CharField(
        max_length=23, choices=enrollments, default="Regular", verbose_name="Enrollment")
    accepted = models.BooleanField(default=False)
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Creation TimeStamp", blank=True)
    lastUpdate = models.DateTimeField(
        auto_now=True, verbose_name="Last Update", blank=True)
