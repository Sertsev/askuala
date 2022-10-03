from asyncio.windows_events import NULL
from datetime import datetime
from pickle import NONE
from turtle import mode
from django.db import models


class Batch(models.Model):
    batchId = models.AutoField(primary_key=True)
    batchName = models.CharField(max_length=63, verbose_name="Batch Name")
    Years = [(r,r) for r in range(2020, datetime.now().year + 1)]
    batchEntryYear = models.PositiveSmallIntegerField(choices=Years, verbose_name="Entry Year")
    batchGraduationYear = models.DateField(verbose_name="Graduation Year")

    def __str__(self):
        return self.batchName

    class Meta:
        ordering = ['batchName']


class Program(models.Model):
    programId = models.AutoField(primary_key=True)
    programName = models.CharField(max_length=63, verbose_name="Program Name")
    programDescription = models.CharField(max_length=63, null=True, verbose_name="Description")
    programInfoLink = models.CharField(max_length=255, null=True, verbose_name="More Information Link")
    resourceAddress = models.CharField(max_length=127, null=True, verbose_name="Resource Address")

    def __str__(self):
        return self.programName


class Department(models.Model):
    departmentId = models.AutoField(primary_key=True)
    departmentName = models.CharField(max_length=127, verbose_name="Department Name")
    departmentDescription = models.CharField(max_length=1023, null=True, verbose_name="Description")
    program = models.ManyToManyField(Program)
    departmentHead = models.CharField(max_length=127, null=True, verbose_name="Department Head")
    resources = models.CharField(max_length=127, null=True)

    def __str__(self):
        return self.departmentName


class Course(models.Model):
    courseId = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=255, verbose_name="Course Name")
    courseDescription = models.CharField(max_length=1023, null=True, verbose_name="Description")
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    resources = models.CharField(max_length=127, null=True)
    
    def __str__(self):
        return self.courseName

    def departmentName(self):
        return self.department.departmentName 


class Courses_in_Batch(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    semester = models.PositiveSmallIntegerField(choices=[(1,1), (2,2)])

    def __str__(self):
        return self.batch.batchName + " " + self.program.programName

    def programName(self):
        return self.program.programName

    def courseName(self):
        return self.course.courseName
    
    def departmentName(self):
        return self.department.departmentName