from django.contrib import admin
from .models import AllAssessment, Assignment


# Register your models here.
# @admin.register(Assignment)
# class AssignmentAdmin(admin.ModelAdmin):
#     list_display = ['assignmentName', 'deadline', 'lecturer',
#                     'course', 'semester', 'year', 'enrollment', 'active']
#     list_editable = ['active', 'enrollment']
#     list_per_page = 10
#     search_fields = ['assignmentName__istartswith']
#     list_filter = ['batch', 'program', 'department']


# @admin.register(AllAssessment)
# class AllAssessmentAdmin(admin.ModelAdmin):
#     list_display = ['student', 'course', 'midExamPoint',
#                     'finalExamPoint', 'total', 'grade']
#     list_per_page = 10
#     list_filter = ['course']
