from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from school_users.permissions import IsGuest, IsLecturer, IsRegistrar, IsStudent
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


"""
    Here under all the get requests of all the users handled here
        anybody with an id or 's url can get results from the 
        following functions
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

    @action(detail=False, methods=['GET', 'PUT'], permission_classes = [IsLecturer])
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


#  Student users api view handler
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['batch_id', 'enrolledProgram_id']
    search_fields = ['firstName', 'middleName', 'lastName']
    ordering_fields = ['firstName', 'lastName', 'lastUpdate']
    permission_classes = [IsRegistrar]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes = [IsStudent])
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

    @action(detail=False)
    def my_courses(self, request):
        pass


#  Guest users api view handlers
class GuestViewSet(ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['educationLevel', 'educationDepartment']
    search_fields = ['firstName', 'middleName', 'lastName']
    ordering_fields = ['firstName', 'lastName', 'lastUpdate']
    permission_classes = [IsRegistrar]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsGuest])
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

    def changePassword(self, request):
        pass

    def logOut(self, request):
        pass


class ACviewSet(ModelViewSet):
    queryset = AssignCourses.objects.select_related('course', 'lecturer', 'batch', 'department').all()
    serializer_class = ACserializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['batch_id', 'course_id', 'department_id']
    permission_classes = [IsRegistrar]
