from tabnanny import verbose
from django.db import models
from school_users.models import *
from programs.models import *

class Assignment(models.Model):
    assignmentId = models.PositiveIntegerField(
        verbose_name="ID", primary_key=True)
    assignmentName = models.CharField(max_length=255, verbose_name="Title")
    assignmentDescription = models.TextField(verbose_name="Description")
    deadline = models.DateTimeField()
    maxMark =  models.PositiveIntegerField()
    lecturer = models.ForeignKey(Lecturer, on_delete=models.PROTECT)
    batch = models.ForeignKey(Batch, on_delete=models.PROTECT)
    program = models.ForeignKey(Program, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    semester = models.PositiveSmallIntegerField(choices=[(1,1), (2,2)])
    year = models.PositiveSmallIntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])
    fileLocation = models.CharField(max_length=127, null=True, blank=True, verbose_name="File Location")
    enrollment = models.CharField(max_length=31, choices=[("Regular", "Regular"), ("Online", "Online")])
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="Assignment Creation TimeStamp", blank=True)
    lastUpdate = models.DateTimeField(auto_now=True, verbose_name="Last Update", blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.assignmentName


class AssignmentPoint(models.Model):
    pointId = models.PositiveBigIntegerField(primary_key=True, verbose_name="ID")
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, null=True, on_delete=models.SET_NULL)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    point = models.PositiveSmallIntegerField()  
    feedback = models.TextField()
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Quiz Creation TimeStamp", blank=True)
    lastUpdate = models.DateTimeField(auto_now=True, verbose_name="Last Update", blank=True)

    def __str__(self):
        return self.student.studentName


class AllAssessment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Student Id")
    course = models.ForeignKey(Course, on_delete=models.PROTECT, verbose_name="Course Id")
    assignmentOnePoint = models.PositiveIntegerField(null=True, blank=True, verbose_name="Assignment 1")
    assignmentTwoPoint = models.PositiveIntegerField(null=True, blank=True, verbose_name="Assignment 2")
    assignmentThreePoint = models.PositiveIntegerField(null=True, blank=True, verbose_name="Assignment 3")
    assignmentFourPoint = models.PositiveIntegerField(null=True, blank=True, verbose_name="Assignment 4")
    quizOnePoint = models.PositiveIntegerField(null=True, blank=True, verbose_name="Quiz 1")
    quizTwoPoint = models.PositiveIntegerField(null=True, blank=True, verbose_name="Quiz 2")
    midExamPoint = models.PositiveIntegerField(null=True, blank=True, verbose_name="Mid-exam")
    finalExamPoint = models.PositiveIntegerField(
        null=True, blank=True, verbose_name="Final Exam")
    total = models.PositiveIntegerField(null=True, blank=True, verbose_name="Total")
    gradeLetter = [
        ('A+', 'A+'), ('A', 'A'), ('A-', 'A-'), 
        ('B+', 'B+'), ('B', 'B'), ('B-', 'B-'), 
        ('C+', 'C+'), ('C', 'C'), ('C-', 'C-'),
        ('D', 'D'), ('Fx', 'Fx'), ('F', 'F'),
        ('NG', 'NG')
        ]
    grade = models.CharField(max_length=3,null=True, blank=True, choices=gradeLetter, verbose_name="Grade")
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Quiz Creation TimeStamp", blank=True)
    lastUpdate = models.DateTimeField(
        auto_now=True, verbose_name="Last Update", blank=True)

    def __str__(self):
        return self.student.studentName


class Quiz(models.Model):
    quizId = models.PositiveIntegerField(verbose_name="ID", primary_key=True)
    quizName = models.CharField(max_length=255, verbose_name="Title")
    quizDescription = models.TextField(verbose_name="Description")
    openingTime = models.DateTimeField(verbose_name="Quiz Opening Time")
    clothingTime = models.DateTimeField(verbose_name="Quiz Clothing Time")
    maxMark = models.PositiveIntegerField()
    lecturer = models.ForeignKey(Lecturer, on_delete=models.PROTECT)
    batch = models.ForeignKey(Batch, on_delete=models.PROTECT)
    program = models.ForeignKey(Program, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    semester = models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2)])
    year = models.PositiveSmallIntegerField(
        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    fileLocation = models.CharField(max_length=127, null=True, blank=True)
    enrollment = models.CharField(max_length=31, choices=[
                                ("Regular", "Regular"), ("Online", "Online")])
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Quiz Creation TimeStamp", blank=True)
    lastUpdate = models.DateTimeField(
        auto_now=True, verbose_name="Last Update", blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.quizName + self.quizId


# class QuizQuestion(models.Model):
#     """_summary_

#     Args:
#         models (_type_): _description_

#     Returns:
#         _type_:
#     """
#     questionId = models.PositiveBigIntegerField(
#         verbose_name="ID", primary_key=True)
#     quizId = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name="ID")
#     questionDetail = models.TextField(verbose_name="Question")
#     imageDir = models.CharField(max_length=127, null=True, blank=True, verbose_name="Image Link")
#     choiceA = models.CharField(max_length=127, null=True, blank=True, verbose_name="Choice A")
#     choiceB = models.CharField(max_length=127, null=True, blank=True, verbose_name="Choice B")
#     choiceC = models.CharField(max_length=127, null=True, blank=True, verbose_name="Choice C")
#     choiceD = models.CharField(max_length=127, null=True, blank=True, verbose_name="Choice D")
#     choiceE = models.CharField(max_length=127, null=True, blank=True, verbose_name="Choice E")
#     choiceF = models.CharField(max_length=127, null=True, blank=True, verbose_name="Choice F")
#     answer = models.CharField(max_length=63)
#     createdAt = models.DateTimeField(
#         auto_now_add=True, verbose_name="Creation TimeStamp", blank=True)
#     lastUpdate = models.DateTimeField(auto_now=True, verbose_name="Last Update", blank=True)


#     def __str__(self):
#         return self.questionId
