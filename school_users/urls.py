from django.urls import path
from .views import *


urlpatterns = [
    path('registrars', registrars_list),
    path('registrar/<int:id>', registrar_info),
    path('lecturers', lecturers_list),
    path('lecturer/<int:id>', lecturer_info),
    path('students', students_list),
    path('student/<int:id>', student_info),
    path('guests', guests_list),
    path('guest/<int:id>', guest_info),
    path('all', all_users),
]