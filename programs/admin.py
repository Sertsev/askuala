from django.contrib import admin

from .models import Batches, Courses, Courses_in_Batch, Department, Program

# Register your models here.
admin.site.register(Program)
admin.site.register(Department)
admin.site.register(Courses)
admin.site.register(Courses_in_Batch)
admin.site.register(Batches)