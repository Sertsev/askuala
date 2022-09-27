from django.contrib import admin

from school_users.models import Guests, Lecturers, Registrars, Students

# Register your models here.
admin.site.register(Students)
admin.site.register(Lecturers)
admin.site.register(Guests)
admin.site.register(Registrars)