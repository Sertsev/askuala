from django.urls import path
from django.urls.conf import include
from .views import *
from rest_framework.routers import SimpleRouter, DefaultRouter

rtr = DefaultRouter()

rtr.register('guests', GuestViewSet)
rtr.register('registrars', RegistrarViewSet)
rtr.register('assigned_courses', ACviewSet)

rtr.register('lecturers', LecturerViewSet)
rtr.register('lecturer/courses', LecturerCourseViewSet)
rtr.register('lecturer/course/lessons', LecturerLessonsViewSet)

rtr.register('students', StudentViewSet)

urlpatterns = [
    path('', include(rtr.urls)),
]