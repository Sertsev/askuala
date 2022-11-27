from django.urls import path
from django.urls.conf import include
from .views import *
from rest_framework.routers import SimpleRouter, DefaultRouter

rtr = DefaultRouter()
rtr.register('lecturers', LecturerViewSet)
rtr.register('students', StudentViewSet)
rtr.register('guests', GuestViewSet)

urlpatterns = [
    path('', include(rtr.urls)),
    path('registrars', Registrars_list),
    path('registrars/<int:id>', Registrar_info),
    path('all', all_users),
]