from datetime import datetime
from turtle import mode
from django.db import models


class Batches(models.Model):
    batchId = models.AutoField(primary_key=True)
    batchName = models.CharField(max_length=63)
    Years = [(r,r) for r in range(2020, datetime.now().year + 1)]
    batchEntryYear = models.PositiveSmallIntegerField(choices=Years)
    batchGraduationYear = models.DateField()

    def __str__(self):
        return self.batchName


class Program(models.Model):
    programId = models.AutoField(primary_key=True)
    programName = models.CharField(max_length=63)
    programDescription = models.CharField(max_length=63, null=True)
    programInfoLink = models.CharField(max_length=255, null=True)
    resourceAddress = models.CharField(max_length=127, null=True)

    def __str__(self):
        return self.programName


class Department(models.Model):
    departmentId = models.AutoField(primary_key=True)
    departmentName = models.CharField(max_length=127)
    departmentDescription = models.CharField(max_length=1023, null=True)
    program = models.ForeignKey(Program, null=True, on_delete=models.SET_NULL)
    departmentHead = models.CharField(max_length=127, null=True)
    resources = models.CharField(max_length=127, null=True)

    def __str__(self):
        return self.departmentName


class Courses(models.Model):
    courseId = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=255)
    courseDescription = models.CharField(max_length=1023, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    resources = models.CharField(max_length=127, null=True)
    
    def __str__(self):
        return self.courseName


class Courses_in_Batch(models.Model):
    batch = models.ForeignKey(Batches, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, null=True, on_delete=models.SET_NULL)
    course = models.ForeignKey(Courses, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    semester = models.PositiveSmallIntegerField(choices=[(1,1), (2,2)])

    def __str__(self):
        return self.batch.batchName + " " + self.program.programName

    def batchName(self):
        return self.batch.batchName
    
    def programName(self):
        return self.program.programName

    def courseName(self):
        return self.course.courseName
    
    def departmentName(self):
        return self.department.departmentName