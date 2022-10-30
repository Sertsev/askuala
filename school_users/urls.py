from django.urls import path
from django.urls.conf import include
from .views import *
from rest_framework.routers import SimpleRouter, DefaultRouter

rtr = DefaultRouter()
rtr.register('registrars', RegistrarViewSet)
rtr.register('students', StudentViewSet)
rtr.register('guests', GuestViewSet)

urlpatterns = [
    path('', include(rtr.urls)),
    path('lecturers', lecturers_list),
    path('lecturer/<int:id>', lecturer_info),
    # path('guests', guests_list),
    # path('guest/<int:id>', guest_info),
    path('all', all_users),
]