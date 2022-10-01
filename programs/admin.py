from django.contrib import admin
from django.db.models.aggregates import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode

from .models import Batch, Course, Courses_in_Batch, Department, Program

# Register your models here.
@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'Number_of_students', 'batchEntryYear', 'batchGraduationYear']
    list_editable = ['batchGraduationYear'] 
    list_per_page = 10
    search_fields = ['batchName']

    @admin.display(ordering="student_count")
    def Number_of_students(self, Batch):
        url = ( # admin:app_model_page
            reverse('admin:school_users_student_changelist')
            + '?'
            + urlencode({
                'batch': str(Batch.batchId)
            }))
        return format_html('<a href="{}">{}</a>', url, Batch.student_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            student_count = Count('student')
        )

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'Number_of_students', 'No_of_lecturers', 'programDescription', 'programInfoLink','resourceAddress']
    list_editable = ['programInfoLink'] 
    list_per_page = 10
    search_fields = ['programName']

    @admin.display(ordering="student_count")
    def Number_of_students(self, Program):
        url = (
            reverse('admin:school_users_student_changelist')
            + '?'
            + urlencode({
                'program': str(Program.programId)
            })
        )
        return format_html('<a href="{}">{}</a>', url, Program.student_count)

    @admin.display(ordering="lecturer_count")
    def No_of_lecturers(self, Program):
        url = (
            reverse('admin:school_users_lecturer_changelist')
            + '?'
            + urlencode({
                'program': str(Program.programId)
            })
        )
        return format_html('<a href="{}">{}</a>', url, Program.lecturer_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            student_count = Count('student'),
            lecturer_count = Count('lecturer'),
        )

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'No_of_students', 'No_of_lecturers', 'departmentDescription', 'departmentHead', 'resources']
    list_editable = ['departmentHead'] 
    list_per_page = 10
    search_fields = ['departmentName']

    @admin.display(ordering="student_count")
    def No_of_students(self, Department):
        url = (
            reverse('admin:school_users_student_changelist')
            + '?'
            + urlencode({
                'department': str(Department.departmentId)
            })
        )
        return format_html('<a href="{}">{}</a>', url, Department.student_count)

    @admin.display(ordering="lecturer_count")
    def No_of_lecturers(self, Department):
        url = (
            reverse('admin:school_users_lecturer_changelist')
            + '?'
            + urlencode({
                'department': str(Department.departmentId)
            })
        )
        return format_html('<a href="{}">{}</a>', url, Department.lecturer_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            student_count = Count('student'),
            lecturer_count = Count('lecturer')
        )
        

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'No_of_students', 'No_of_guests', 'No_of_lecturers', 'courseDescription', 'department', 'resources']
    # list_editable = ['departmentName']
    list_per_page = 10

    @admin.display(ordering="student_count")
    def No_of_students(self, Course):
        url = (
            reverse('admin:school_users_student_changelist')
            + '?'
            + urlencode({
                'course': str(Course.courseId)
            })
        )
        return format_html('<a href="{}">{}</a>', url, Course.student_count)

    @admin.display(ordering="guest_count")
    def No_of_guests(self, Course):
        url = (
            reverse('admin:school_users_guest_changelist')
            + '?'
            + urlencode({
                'course': str(Course.courseId)
            })
        )
        return format_html('<a href="{}">{}</a>', url, Course.guest_count)

    @admin.display(ordering="lecturer_count")
    def No_of_lecturers(self, Course):
        url = (
            reverse('admin:school_users_lecturer_changelist')
            + '?'
            + urlencode({
                'course': str(Course.courseId)
            })
        )
        return format_html('<a href="{}">{}</a>', url, Course.lecturer_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            student_count = Count('student'),
            guest_count = Count('guest'),
            lecturer_count = Count('lecturer')
        )


@admin.register(Courses_in_Batch)
class CBAdmin(admin.ModelAdmin):
    list_display = ['__str__','batch_name', 'program', 'course', 'department', 'semester']
    list_editable = ['semester']
    list_per_page = 10
    # list_select_related = ['batch']

    # @admin.
    def batch_name(self, Courses_in_Batch):
        return Courses_in_Batch.batch.batchName
