from tabnanny import verbose
from django.db import models
from school_users.models import *
from programs.models import *

class Assignment(models.Model):
    assignmentId = models.PositiveIntegerField(
        verbose_name="ID", primary_key=True)
    assignmentName = models.CharField(max_length=255, verbose_name="Title")
    assignmentDescription = models.TextField(verbose_name="Description")
    deadline = models.DateField()
    batch = models.ForeignKey(Batch, on_delete=models.PROTECT)
    program = models.ForeignKey(Program, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    semester = models.PositiveSmallIntegerField(choices=[(1,1), (2,2)])
    year = models.PositiveSmallIntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])
    fileLocation = models.CharField(max_length=127, null=True, blank=True, verbose_name="File Location")
    enrollment = models.CharField(max_length=31, choices=[("Regular", "Regular"), ("Online", "Online")])
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="Assignment Creation TimeStamp")
    lastUpdate = models.DateField(auto_now=True, verbose_name="Last Update")
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.assignmentName


class Quiz(models.Model):
    quizId = models.PositiveIntegerField(verbose_name="ID", primary_key=True)
    quizName = models.CharField(max_length=255, verbose_name="Title")
    quizDescription = models.TextField(verbose_name="Description")
    openingTime = models.DateTimeField(verbose_name="Quiz Opening Time")
    clothingTime = models.DateTimeField(verbose_name="Quiz Clothing Time")
    batch = models.ForeignKey(Batch, on_delete=models.PROTECT)
    program = models.ForeignKey(Program, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    semester = models.PositiveSmallIntegerField(choices=[(1,1), (2,2)])
    year = models.PositiveSmallIntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])
    fileLocation = models.CharField(max_length=127, null=True, blank=True)
    enrollment = models.CharField(max_length=31, choices=[("Regular", "Regular"), ("Online", "Online")])
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="Quiz Creation TimeStamp")
    lastUpdate = models.DateField(auto_now=True, verbose_name="Last Update")
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.quizName


class QuizQuestion(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: 
    """
    questionId = models.PositiveBigIntegerField(
        verbose_name="ID", primary_key=True)
    quizId = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name="ID")
    questionDetail = models.TextField(verbose_name="Question")
    imageDir = models.CharField(max_length=127, null=True, blank=True, verbose_name="Image Link")
    choiceA = models.CharField(max_length=127, null=True, blank=True, verbose_name="Choice A")
    choiceB = models.CharField(max_length=127, null=True, blank=True, verbose_name="Choice B")
    choiceC = models.CharField(max_length=127, null=True, blank=True, verbose_name="Choice C")
    choiceD = models.CharField(max_length=127, null=True, blank=True, verbose_name="Choice D")
    choiceE = models.CharField(max_length=127, null=True, blank=True, verbose_name="Choice E")
    choiceF = models.CharField(max_length=127, null=True, blank=True, verbose_name="Choice F")
    answer = models.CharField(max_length=63)
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="Creation TimeStamp")
    lastUpdate = models.DateField(auto_now=True, verbose_name="Last Update")
    

    def __str__(self):
        return self.questionId


class Point(models.Model):
    pointId = models.PositiveBigIntegerField(primary_key=True, verbose_name="ID")
    assessmentType = models.CharField(max_length=63, choices=[('Quiz', 'Quiz'), ('Assignment', ('Assignment'))],verbose_name="Assessment Type")
    assessmentId = models.PositiveBigIntegerField(verbose_name="Assessment ID")
    studentId = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecturerId = models.ForeignKey(Lecturer, null=True, on_delete=models.SET_NULL)
    feedback = models.TextField()
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Quiz Creation TimeStamp")
    lastUpdate = models.DateField(auto_now=True, verbose_name="Last Update")
