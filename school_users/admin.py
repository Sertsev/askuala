from django.contrib import admin
from school_users.models import Guests, Lecturers, Registrars, Students


@admin.register(Guests)
class GuestsAdmin(admin.ModelAdmin):
    list_display = ['fullName', 'email', 'educationLevel', 'educationDepartment', 'active', 'lastUpdate']
    list_editable = ['active']
    list_per_page = 10


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['fullName', 'email', 'previousEducationLevel', 'previousEducationDepartment', 'academicYear', 'active', 'verified', 'enrollment_type']
    list_editable = ['active', 'academicYear', 'verified', 'enrollment_type']
    list_per_page = 10


@admin.register(Lecturers)
class LecturersAdmin(admin.ModelAdmin):
    list_display = ['fullName', 'email', 'educationLevel', 'educationDepartment', 'active', 'verified', 'lastUpdate']
    list_editable = ['active', 'verified']
    list_per_page = 10


@admin.register(Registrars)
class RegistrarsAdmin(admin.ModelAdmin):
    list_display = ['fullName', 'email', 'educationLevel', 'educationDepartment', 'active', 'lastUpdate']
    list_editable = ['active']
    list_per_page = 10