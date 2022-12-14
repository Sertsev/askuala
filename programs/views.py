from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser

from .permissions import IsRegistrarOrReadOnly
from .models import *
from .serializers import *

# Batch view handler
class BatchViewSet(ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    filter_backends = [SearchFilter]
    search_fields = ['batchName']
    permission_classes = [IsRegistrarOrReadOnly]

    def get_view_name(self):
        return "Batches List"



# Degree or Program view handler
class ProgramViewSet(ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    filter_backends = [SearchFilter]
    search_fields = ['programName', 'programDescription']
    permission_classes = [IsRegistrarOrReadOnly]


# Department view handler
class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['departmentName', 'departmentDescription', 'departmentHead']
    permission_classes = [IsRegistrarOrReadOnly]


# Course view handler
class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields =  ['department_id']
    search_fields = ['courseName', 'courseDescription']
    permission_classes = [IsRegistrarOrReadOnly]


# Course in batch view handler
class CIBViewSet(ModelViewSet):
    queryset = Courses_in_Batch.objects.select_related('program', 'batch', 'department', 'course').all()
    serializer_class = CiBSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['department_id', 'batch_id', 'program_id']
    search_fields = ['course__courseName']
    permission_classes = [IsAdminUser, IsRegistrarOrReadOnly]

    def get_view_name(self):
        return "Courses Enrolled to Batches List"


# Lesson view handler
class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields =  ['course_id']
    search_fields = ['lessonName', 'lessonDescription']
    permission_classes = [IsAdminUser, IsRegistrarOrReadOnly]
