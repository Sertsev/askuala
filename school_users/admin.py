from django.contrib import admin, messages
from django.utils.html import format_html, urlencode
from school_users.models import Guest, Lecturer, Registrar, Student

@admin.register(Guest)
class GuestsAdmin(admin.ModelAdmin):
    actions = ['activate', 'deactivate']
    list_display = ['full_name', 'email', 'educationLevel', 'educationDepartment', 'active', 'lastUpdate']
    list_editable = ['active', 'educationDepartment']
    list_per_page = 10
    list_filter = ['educationLevel', 'educationDepartment']
    search_fields = ['firstName__istartswith', 'middleName__istartswith', 'lastName__istartswith',]

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
        'documentLocation': ['firstName']
    }
    actions = ['activate', 'deactivate']
    list_display = ['full_name', 'email', 'batch_name', 'current_program', 'academicYear', 'active', 'verified', 'enrollment_type']
    list_editable = ['active', 'academicYear', 'enrollment_type']
    list_per_page = 10
    list_filter = ['batch', 'program']
    search_fields = ['firstName__startswith', 'middleName__startswith', 'lastName__istartswith']#__startswith', 'batch__istartswith', 'program__istartswith', 'enrollment_type__istartswith']

    @admin.display(ordering="program")
    def current_program(self, Student):
        url = ( 
            '/admin/programs/program/'
            + str(Student.program.programId)
            + '/change')
        return format_html('<a href="{}">{}</a>', url, Student.program)

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
    list_display = ['full_name', 'email', 'educationLevel', 'educationDepartment', 'active', 'verified', 'lastUpdate']
    list_editable = ['educationDepartment', 'active']
    list_per_page = 10
    list_filter = ['educationLevel', 'educationDepartment']
    search_fields = ['firstName__istartswith', 'middleName__istartswith', 'lastName__istartswith']

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
    list_display = ['full_name', 'email', 'educationLevel', 'educationDepartment', 'active', 'lastUpdate']
    list_editable = ['active']
    list_per_page = 10
    list_filter = ['educationLevel']
    search_fields = ['firstName__istartswith', 'middleName__istartswith', 'lastName__istartswith']

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