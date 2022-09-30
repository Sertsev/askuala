from django.contrib import admin
from school_users.models import Guests, Lecturers, Registrars, Students

@admin.register(Guests)
class GuestsAdmin(admin.ModelAdmin):
    list_display = ['guestId', 'firstName', 'middleName', 'lastName', 'email', 'phoneNumber', 'educationLevel', 'educationDepartment', 'active']
    list_editable = ['educationLevel', 'educationDepartment', 'active']
    list_per_page = 20

# Register your models here.
admin.site.register(Students)
admin.site.register(Lecturers)
# admin.site.register(Guests)
admin.site.register(Registrars)