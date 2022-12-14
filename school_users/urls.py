from django.urls import path
from django.urls.conf import include
from .views import *
from rest_framework.routers import SimpleRouter, DefaultRouter

rtr = DefaultRouter()
rtr.register('lecturers', LecturerViewSet)
rtr.register('students', StudentViewSet)
rtr.register('guests', GuestViewSet)
rtr.register('registrars', RegistrarViewSet)
rtr.register('assigned_courses', ACviewSet)

urlpatterns = [
    path('', include(rtr.urls)),
]