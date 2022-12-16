from django.db import models
from school_users.models import *
from programs.models import *

class Assignment(models.Model):
    assignmentId = models.PositiveIntegerField(verbose_name="ID", primary_key=True)
    assignmentTitle = models.CharField(max_length=255, verbose_name="Title")
    assignmentDescription = models.TextField(verbose_name="Description")
    maxPoint = models.PositiveSmallIntegerField()
    lecturer = models.ForeignKey(Lecturer, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    fileLocation = models.CharField(max_length=127, null=True, blank=True, verbose_name="File Location")
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="Assignment Creation TimeStamp", blank=True)
    lastUpdate = models.DateTimeField(auto_now=True, verbose_name="Last Update", blank=True)
    active = models.BooleanField()

    def __str__(self):
        return self.assignmentTitle


class GivenAssignments(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.PROTECT)
    batch = models.ForeignKey(Batch, models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    deadline = models.DateTimeField()
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Assignment Creation TimeStamp", blank=True)
    lastUpdate = models.DateTimeField(
        auto_now=True, verbose_name="Last Update", blank=True)
    active = models.BooleanField()


class AssignmentPoint(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.PROTECT)
    point = models.PositiveSmallIntegerField()
    maxPoint = models.PositiveSmallIntegerField()
    feedback = models.TextField()
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Quiz Creation TimeStamp", blank=True)
    lastUpdate = models.DateTimeField(auto_now=True, verbose_name="Last Update", blank=True)

    def __str__(self):
        return self.student.studentName


class Quiz(models.Model):
    quizId = models.PositiveIntegerField(verbose_name="ID", primary_key=True)
    quizTitle = models.CharField(max_length=255, verbose_name="Title")
    quizDescription = models.TextField(verbose_name="Description")
    maxPoint = models.PositiveSmallIntegerField()
    givenTime = models.PositiveSmallIntegerField()
    lecturer = models.ForeignKey(Lecturer, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    fileLocation = models.CharField(max_length=127, null=True, blank=True)
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Quiz Creation TimeStamp", blank=True)
    lastUpdate = models.DateTimeField(
        auto_now=True, verbose_name="Last Update", blank=True)
    active = models.BooleanField()

    def __str__(self):
        return self.quizTitle


class GivenQuiz(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.PROTECT)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    openingTime = models.DateTimeField(verbose_name="Quiz Opening Time")
    clothingTime = models.DateTimeField(verbose_name="Quiz Clothing Time")
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Assignment Creation TimeStamp", blank=True)
    lastUpdate = models.DateTimeField(
        auto_now=True, verbose_name="Last Update", blank=True)
    active = models.BooleanField()

    def __str__(self) -> str:
        return self.quiz.quizTitle


class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    questionTitle = models.CharField(max_length=255, verbose_name="Title")
    questionDetail = models.TextField(verbose_name="Question")
    fileLocation = models.CharField(max_length=127, null=True, blank=True, verbose_name="Image Link")
    choiceA = models.CharField(max_length=127, null=True, blank=True, verbose_name="Choice A")
    choiceB = models.CharField(max_length=127, null=True, blank=True, verbose_name="Choice B")
    choiceC = models.CharField(max_length=127, null=True, blank=True, verbose_name="Choice C")
    choiceD = models.CharField(max_length=127, null=True, blank=True, verbose_name="Choice D")
    choiceE = models.CharField(max_length=127, null=True, blank=True, verbose_name="Choice E")
    choiceF = models.CharField(max_length=127, null=True, blank=True, verbose_name="Choice F")
    choiceG = models.CharField(
        max_length=127, null=True, blank=True, verbose_name="Choice G")
    answer = models.CharField(max_length=127) # encrypted
    givenTime = models.PositiveSmallIntegerField(null=True, blank=True) # put minutes
    maxPoint = models.PositiveSmallIntegerField(null=True, blank=True)
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Creation TimeStamp", blank=True)
    lastUpdate = models.DateTimeField(auto_now=True, verbose_name="Last Update", blank=True)


    def __str__(self):
        return self.questionTitle


class QuizPoint(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.PROTECT)
    point = models.PositiveSmallIntegerField()
    maxPoint = models.PositiveSmallIntegerField()
    feedback = models.TextField()
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Quiz Creation TimeStamp", blank=True)
    lastUpdate = models.DateTimeField(
        auto_now=True, verbose_name="Last Update", blank=True)

    def __str__(self):
        return self.student.studentName


class AllAssessment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Student Id")
    course = models.ForeignKey(Course, on_delete=models.PROTECT, verbose_name="Course Id")
    assignmentOnePoint = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Assignment 1")
    assignmentTwoPoint = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Assignment 2")
    quizOnePoint = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Quiz 1")
    midExamPoint = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Mid-exam")
    finalExamPoint = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="Final Exam")
    total = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="Total")
    grade = models.CharField(max_length=3,null=True, blank=True, verbose_name="Grade")
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Quiz Creation TimeStamp", blank=True)
    lastUpdate = models.DateTimeField(
        auto_now=True, verbose_name="Last Update", blank=True)

    def __str__(self):
        return self.student.studentName
