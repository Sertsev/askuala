from django.urls import path
from .views import *

urlpatterns = [
    path('batches', all_batches),
    path('batch/<int:pk>', batch_info),
    path('degrees', all_degrees),
    path('degree/<int:pk>', degree_info),
    path('departments', all_departments),
    path('department/<int:pk>', department_info),
    path('courses', all_courses),
    path('course/<int:pk>', course_info),
    path('cib', all_cib),
    path('cib/<int:pk>', cib_info),
    path('lessons', all_lessons),
    path('lesson/<int:pk>', lesson_info)
]