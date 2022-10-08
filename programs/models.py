from datetime import datetime
from django.db import models

class Batch(models.Model):
    batchId = models.AutoField(primary_key=True)
    batchName = models.CharField(max_length=63, verbose_name="Batch Name")
    batchProgram = models.CharField(max_length=23, choices=[('Master', 'Master'), ('Bachelor', 'Bachelor')], verbose_name="Batch Program")
    Years = [(r,r) for r in range(2020, datetime.now().year + 1)]
    batchEntryYear = models.PositiveSmallIntegerField(choices=Years, verbose_name="Entry Year")
    batchGraduationYear = models.DateField(verbose_name="Graduation Year")
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="Creation TimeStamp")
    lastUpdate = models.DateField(auto_now=True, verbose_name="Last Update")

    def __str__(self):
        return self.batchName

    class Meta:
        ordering = ['batchName']


class Program(models.Model):
    programId = models.AutoField(primary_key=True)
    programName = models.CharField(max_length=63, verbose_name="Program Name")
    programDescription = models.CharField(max_length=63, null=True, verbose_name="Description", blank=True)
    programInfoLink = models.CharField(max_length=255, null=True, verbose_name="More Information Link", blank=True)
    resourceAddress = models.CharField(max_length=127, null=True, verbose_name="Resource Address", blank=True)
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Creation TimeStamp")
    lastUpdate = models.DateField(auto_now=True, verbose_name="Last Update")

    def __str__(self):
        return self.programName


class Department(models.Model):
    departmentId = models.AutoField(primary_key=True)
    departmentName = models.CharField(max_length=127, verbose_name="Department Name")
    departmentDescription = models.CharField(max_length=1023, null=True, verbose_name="Description", blank=True)
    program = models.ManyToManyField(Program)
    departmentHead = models.CharField(max_length=127, verbose_name="Department Head")
    # departmentHead = models.ForeignKey('school_users.Lecturer', on_delete=models.PROTECT)
    resources = models.CharField(max_length=127, null=True, blank=True)
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Creation TimeStamp")
    lastUpdate = models.DateField(auto_now=True, verbose_name="Last Update")
    

    def __str__(self):
        return self.departmentName


class Course(models.Model):
    courseId = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=255, verbose_name="Course Name")
    courseDescription = models.TextField(null=True, verbose_name="Description", blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    resources = models.CharField(max_length=127, null=True, blank=True)
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Creation TimeStamp")
    lastUpdate = models.DateField(auto_now=True, verbose_name="Last Update")
    
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
    year = models.PositiveSmallIntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Creation TimeStamp")
    lastUpdate = models.DateField(auto_now=True, verbose_name="Last Update")

    def __str__(self):
        return self.batch.batchName + " " + self.program.programName

    def programName(self):
        return self.program.programName

    def courseName(self):
        return self.course.courseName
    
    def departmentName(self):
        return self.department.departmentName