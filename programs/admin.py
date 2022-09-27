from django.contrib import admin

from .models import Courses, Department, Program

# Register your models here.
admin.site.register(Program)
admin.site.register(Department)
admin.site.register(Courses)