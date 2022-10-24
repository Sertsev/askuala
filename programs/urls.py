from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter


rtr = DefaultRouter()
rtr.register('batches', BatchViewSet)
rtr.register('degrees', ProgramViewSet)
rtr.register('departments', DepartmentViewSet)
rtr.register('courses', CourseViewSet)
rtr.register('cib', CIBViewSet)
rtr.register('lessons', LessonViewSet)

urlpatterns = rtr.urls