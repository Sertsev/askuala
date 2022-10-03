from django.contrib import admin
from school_users.models import Guest, Lecturer, Registrar, Student


@admin.register(Guest)
class GuestsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'educationLevel', 'educationDepartment', 'active', 'lastUpdate']
    list_editable = ['active', 'educationDepartment']
    list_per_page = 10
    list_filter = ['educationLevel', 'educationDepartment']
    search_fields = ['firstName__istartswith', 'middleName__istartswith', 'lastName__istartswith',]


@admin.register(Student)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'batch', 'program', 'academicYear', 'active', 'verified', 'enrollment_type']
    list_editable = ['active', 'academicYear', 'verified', 'enrollment_type']
    list_per_page = 10
    list_filter = ['batch', 'program']
    search_fields = ['firstName__startswith', 'middleName__startswith', 'lastName__istartswith']#__startswith', 'batch__istartswith', 'program__istartswith', 'enrollment_type__istartswith']


@admin.register(Lecturer)
class LecturersAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'educationLevel', 'educationDepartment', 'active', 'verified', 'lastUpdate']
    list_editable = ['educationDepartment', 'active', 'verified']
    list_per_page = 10
    list_filter = ['educationLevel', 'educationDepartment', 'program']
    search_fields = ['firstName__istartswith', 'middleName__istartswith', 'lastName__istartswith']


@admin.register(Registrar)
class RegistrarsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'educationLevel', 'educationDepartment', 'active', 'lastUpdate']
    list_editable = ['active']
    list_per_page = 10
    list_filter = ['educationLevel']
    search_fields = ['firstName__istartswith', 'middleName__istartswith', 'lastName__istartswith']