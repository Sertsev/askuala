from django.contrib import admin, messages
from django.utils.html import format_html, urlencode
from .models import Guest, Lecturer, Registrar, Student, User, AssignCourses
from django.contrib.auth.admin import UserAdmin as UA
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserAdmin(UA):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "middle_name", "last_name", "gender", "email", "phone_number", "user_type")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("user_type", "username", "first_name", "middle_name", "last_name", "gender", "password1", "password2", "email", "phone_number"),
            },
        ),
    )
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "user_type")
    list_editable = ["user_type"]


@admin.register(Guest)
class GuestsAdmin(admin.ModelAdmin):
    actions = ['activate', 'deactivate']
    list_display = ['full_name', 'educationLevel', 'educationDepartment', 'lastUpdate']
    list_per_page = 10
    list_filter = ['educationLevel', 'educationDepartment']
    search_fields = ['user__first_name__istartswith', 'user__middle_name__istartswith', 'user__last_name__istartswith']

    @admin.action(description=('Deactivate selected guests'))
    def deactivate(self, request, queryset):
        update_count = queryset.update(active=0)
        self.message_user(
            request,
            f'{update_count} number of students successfully Deactivated.',
            messages.SUCCESS)

    @admin.action(description=('Activate selected guests'))
    def activate(self, request, queryset):
        update_count = queryset.update(active=1)
        self.message_user(
            request,
            f'{update_count} number of students successfully Activated.',
            messages.SUCCESS)


@admin.register(Student)
class StudentsAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'documentLocation': ['user']
    }
    actions = ['activate', 'deactivate']
    list_display = ['full_name', 'batch_name',
                    'current_program', 'current_dep', 'enrollment_type']
    list_editable = ['enrollment_type']
    list_per_page = 10
    list_filter = ['batch', 'enrolledProgram', 'enrolledDepartment']
    search_fields = ['user__first_name__istartswith',
                        'user__middle_name__istartswith', 'user__last_name__istartswith']

    @admin.display(ordering="enrolledProgram")
    def current_program(self, Student):
        url = ( 
            '/admin/programs/program/'
            + str(Student.enrolledProgram.programId)
            + '/change')
        return format_html('<a href="{}">{}</a>', url, Student.enrolledProgram)

    @admin.display(ordering="enrolledDepartment")
    def current_dep(self, Student):
        url = ( 
            '/admin/programs/department/'
            + str(Student.enrolledDepartment.departmentId)
            + '/change')
        return format_html('<a href="{}">{}</a>', url, Student.enrolledDepartment)

    @admin.display(ordering="batch")
    def batch_name(self, Student):
        url = ( 
            '/admin/programs/batch/'
            + str(Student.batch.batchId)
            + '/change')
        return format_html('<a href="{}">{}</a>', url, Student.batch) 

    @admin.action(description=('Deactivate selected students'))
    def deactivate(self, request, queryset):
        update_count = queryset.update(active=0)
        self.message_user(
            request,
            f'{update_count} number of students successfully Deactivated.',
            messages.SUCCESS)

    @admin.action(description=('Activate selected students'))
    def activate(self, request, queryset):
        update_count = queryset.update(active=1)
        self.message_user(
            request,
            f'{update_count} number of students successfully Activated.',
            messages.SUCCESS)
        

@admin.register(Lecturer)
class LecturersAdmin(admin.ModelAdmin):
    actions = ['activate', 'deactivate']
    list_display = ['full_name', 'educationLevel', 'educationDepartment', 'lastUpdate']
    list_editable = ['educationDepartment']
    list_per_page = 10
    list_filter = ['educationLevel', 'educationDepartment']
    search_fields = ['user__first_name__istartswith',
                        'user__middle_name__istartswith', 'user__last_name__istartswith']

    @admin.action(description=('Deactivate selected lecturers'))
    def deactivate(self, request, queryset):
        update_count = queryset.update(active=0)
        self.message_user(
            request,
            f'{update_count} number of students successfully Deactivated.',
            messages.SUCCESS)

    @admin.action(description=('Activate selected lecturers'))
    def activate(self, request, queryset):
        update_count = queryset.update(active=1)
        self.message_user(
            request,
            f'{update_count} number of students successfully Activated.',
            messages.SUCCESS)


@admin.register(Registrar)
class RegistrarsAdmin(admin.ModelAdmin):
    actions = ['activate', 'deactivate']
    list_display = ['full_name', 'educationLevel', 'educationDepartment', 'lastUpdate']
    list_per_page = 10
    list_filter = ['educationLevel']
    search_fields = ['user__first_name__istartswith', 'user__middle_name__istartswith', 'user__last_name__istartswith']

    @admin.action(description=('Deactivate selected registrars'))
    def deactivate(self, request, queryset):
        update_count = queryset.update(active=0)
        self.message_user(
            request,
            f'{update_count} number of students successfully Deactivated.',
            messages.SUCCESS)

    @admin.action(description=('Activate selected registrars'))
    def activate(self, request, queryset):
        update_count = queryset.update(active=1)
        self.message_user(
            request,
            f'{update_count} number of students successfully Activated.',
            messages.SUCCESS)


@admin.register(AssignCourses)
class ACadmin(admin.ModelAdmin):
    list_display = ['__str__', 'lecturer', 'course_type', 'lastUpdate']
    list_per_page = 10
    list_filter = ['course']
