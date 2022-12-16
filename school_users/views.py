from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
# from rest_framework.authentication.

from programs.models import Courses_in_Batch, Lesson
from programs.serializers import SimpleCiBSerializer, LessonSerializer, LessonCreateSerializer 
from .permissions import *
from .models import *
from .serializers import *


"""
    Here under all the get requests of all the users handled here
        anybody with an id or 's url can get results from the 
        following classes
"""


#  Registrar users api view handler
class RegistrarViewSet(ModelViewSet):
    queryset = Registrar.objects.all()
    serializer_class = RegistrarSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["educationDepartment"]
    search_fields = ['firstName', 'middleName', 'lastName']
    ordering_fields = ['firstName', 'lastName', 'lastUpdate']
    permission_classes = [permissions.IsAdminUser]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsRegistrar])
    def my_profile(self, request):
        (registrar, created) = Registrar.objects.select_related('user').get_or_create(
            user_id=request.user.id)
        if request.method == 'GET':
            registrarSerialized = RegistrarSerializer(registrar)
            return Response(registrarSerialized.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            registrarSerialized = RegistrarSerializer(
                registrar, data=request.data, partial=True)
            registrarSerialized.is_valid(raise_exception=True)
            registrarSerialized.save()
            return Response(registrarSerialized.data, status=status.HTTP_200_OK)


#  Lecturer users api view handlers
class LecturerViewSet(ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["educationDepartment"]
    search_fields = ['firstName', 'middleName', 'lastName']
    ordering_fields = ['firstName', 'lastName', 'lastUpdate']
    permission_classes = [IsRegistrar]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes = [IsLecturer], filter_backends=[])
    def my_profile(self, request):
        (lecturer, created) = Lecturer.objects.select_related('user').get_or_create(
            user_id=request.user.id)
        if request.method == 'GET':
            lecturerSerialized = LecturerSerializer(lecturer)
            return Response(lecturerSerialized.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            lecturerSerialized = LecturerSerializer(
                lecturer, data=request.data, partial=True)
            lecturerSerialized.is_valid(raise_exception=True)
            lecturerSerialized.save()
            return Response(lecturerSerialized.data, status=status.HTTP_200_OK)


class LecturerCourseViewSet(ModelViewSet):
    queryset = AssignCourses.objects.all()
    serializer_class = AClecturerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['course__courseName']
    filterset_fields=["department"]
    ordering_fields = ['course']
    permission_classes=[IsLecturer] 

    def get_queryset(self):
        lecturer = get_object_or_404(Lecturer, user_id=self.request.user.id)
        serialized = SimpleLecturerSerializer(lecturer)
        queryset = AssignCourses.objects.filter(lecturer_id=serialized.data['lecturerId']).all()
        return queryset

    def _allowed_methods(self):
        return permissions.SAFE_METHODS


class LecturerLessonsViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonCreateSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['course']
    search_fields = ['lessonName']
    ordering_fields = ['lessonName']
    permission_classes = [IsLecturer]

    def get_queryset(self):
        return Lesson.objects.filter(lecturer_id=self.request.user.id).all()

    def create(self, request, *args, **kwargs):
        if request.data['lecturer'] == request.user.id:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response('Please select proper user')


#  Student users api view handler
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['batch_id', 'enrolledProgram_id']
    search_fields = ['user__first_name', 'user__middle_name', 'user__last_name']
    ordering_fields = ['user__first_name', 'user__last_name', 'lastUpdate']
    permission_classes = [IsRegistrar]

    # defining the queryset for each user_type
    def get_queryset(self):
        if self.request.user.user_type == 'registrar':
            return super().get_queryset()
        elif self.request.user.user_type == 'student':
            student = get_object_or_404(Student, user_id=self.request.user.id)
            serialized = SimpleStudentSerializer(student)
            return Student.objects.filter(batch_id=serialized.data['batch']['batchId'],
                                        enrolledDepartment_id=serialized.data['enrolledDepartment']['departmentId']).all()
    
    # defining the http methods for each user_type
    def _allowed_methods(self):
        if self.request.user.user_type == 'student':
            self.filter_backends = [SearchFilter, OrderingFilter]
            return permissions.SAFE_METHODS
        elif self.request.user.user_type == 'registrar':
            return permissions.SAFE_METHODS + ('POST', 'PUT')

    # defining the permissions for each user_type
    def get_permissions(self):
        if self.request.user.user_type == 'student':
            return (IsStudent(),)
        return super().get_permissions()

    # my profile page for the user
    @action(detail=False, methods=['GET', 'PUT'], permission_classes = [IsStudent], filter_backends=[])
    def my_profile(self, request):
        (student, created) = Student.objects.select_related('user').get_or_create(
            user_id=request.user.id)
        if request.method == 'GET':
            studentSerialized = StudentSerializer(student)
            return Response(studentSerialized.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            studentSerialized = StudentSerializer(
                student, data=request.data, partial=True)
            studentSerialized.is_valid(raise_exception=True)
            studentSerialized.save()
            return Response(studentSerialized.data, status=status.HTTP_200_OK)

    @action(detail=False, 
            methods=['GET'], 
            permission_classes=[IsStudent], 
            filter_backends=[])
    def my_courses(self, request):
        student = get_object_or_404(Student, user_id=request.user.id)
        serialized = SimpleStudentSerializer(student)
        courses = get_list_or_404(
            Courses_in_Batch, batch_id=serialized.data['batch']['batchId'], 
            department_id=serialized.data['enrolledDepartment']['departmentId'],
            program_id=serialized.data['enrolledProgram']['programId'])
        serialized = SimpleCiBSerializer(courses, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)


#  Guest users api view handlers
class GuestViewSet(ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['educationLevel', 'educationDepartment']
    search_fields = ['firstName', 'middleName', 'lastName']
    ordering_fields = ['firstName', 'lastName', 'lastUpdate']
    permission_classes = [IsRegistrar]

    @action(detail=False, 
            methods=['GET', 'PUT'], 
            permission_classes=[IsGuest], 
            filter_backends=[])
    def my_profile(self, request):
        (guest, created) = Guest.objects.select_related('user').get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            guestsSerialized = GuestSerializer(guest)
            return Response(guestsSerialized.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            guestsSerialized = GuestSerializer(guest, data=request.data, partial=True)
            guestsSerialized.is_valid(raise_exception=True)
            guestsSerialized.save()
            return Response(guestsSerialized.data, status=status.HTTP_200_OK)


class ACviewSet(ModelViewSet):
    queryset = AssignCourses.objects.select_related(
        'course', 'lecturer', 'department').all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['course_id', 'department_id']
    permission_classes = [IsRegistrar]
    serializer_class = ACserializer

    def get_view_name(self):
        return "Assigned Courses to Lecturers List"

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return ACserializer
        return ACcreateSerializer

    def perform_create(self, serializer):
        serializer.save(registrar=self.request.user)
