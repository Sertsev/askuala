from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['course', 'lecturer', 'assignmentTitle', 'maxPoint', 'active']
    list_per_page = 10
    list_filter = ['course']
    list_editable = ['active']


@admin.register(GivenAssignments)
class GivenAssignmentsAdmin(admin.ModelAdmin):
    list_display = ['batch', 'department',
                    'assignment', 'deadline', 'active']
    list_per_page = 10
    list_filter = ['batch', 'department']
    list_editable = ['active']


@admin.register(AssignmentPoint)
class AssignmentPointAdmin(admin.ModelAdmin):
    list_display = ['student', 'assignment', 'point', 'maxPoint']
    list_per_page = 10
    list_filter = ['assignment']


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['course', 'quizTitle', 'maxPoint', 'givenTime', 'lecturer', 'active']
    list_per_page = 10
    list_filter = ['course']
    list_editable = ['active']


@admin.register(GivenQuiz)
class GivenQuizAdmin(admin.ModelAdmin):
    list_display = ['batch', 'department', 'quiz', 'openingTime', 'clothingTime', 'active']
    list_per_page = 10
    list_filter = ['batch', 'department']
    list_editable = ['active']


@admin.register(QuizPoint)
class QuizPointAdmin(admin.ModelAdmin):
    list_display = ['student', 'quiz', 'point', 'maxPoint']
    list_per_page = 10
    list_filter = ['quiz']


@admin.register(AllAssessment)
class AllAssessmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'midExamPoint',
                    'finalExamPoint', 'total', 'grade']
    list_per_page = 10
    list_filter = ['course']
