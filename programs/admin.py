from django.contrib import admin

from .models import Batches, Courses, Courses_in_Batch, Department, Program

# Register your models here.
admin.site.register(Batches)
admin.site.register(Program)
admin.site.register(Department)
admin.site.register(Courses)


@admin.register(Courses_in_Batch)
class CBAdmin(admin.ModelAdmin):
    list_display = ['__str__','batchName', 'programName', 'courseName', 'departmentName', 'semester']
    list_editable = ['semester']
    list_per_page = 10
