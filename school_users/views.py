from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

"""
    Here under all the get requests of all the users handled here
        anybody with an id or 's url can get results from the 
        following functions
"""

#  Registrar users api view handlers
@api_view()
def registrars_list(request):
    queryset =  get_list_or_404(Registrar)
    serializer =  RegistrarSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def registrar_info(request, id):
    registrar = get_object_or_404(Registrar, pk=id)
    serializer = RegistrarSerializer(registrar)
    return Response(serializer.data)


#  Lecturer users api view handlers
@api_view()
def lecturers_list(request):
    queryset = get_list_or_404(Lecturer)
    serializer = LecturerSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def lecturer_info(request, id):
    lecturer = get_object_or_404(Lecturer, pk=id)
    serializer = LecturerSerializer(lecturer)
    return Response(serializer.data)


#  Student users api view handlers
@api_view()
def students_list(request):
    queryset = Student.objects.select_related('program').all()
    serializer = StudentSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def student_info(request, id):
    student = get_object_or_404(Student, pk=id)
    serializer = StudentSerializer(student)
    return Response(serializer.data)


#  Guest users api view handlers
@api_view()
def guests_list(request):
    queryset = get_list_or_404(Guest)
    serializer = GuestSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def guest_info(request, id):
    guest = get_object_or_404(Guest, pk=id)
    serializer = GuestSerializer(guest)
    return Response(serializer.data)


# To see all users
@api_view()
def all_users(request):
    # getting guests list
    guestsSerialized = GuestSerializer(get_list_or_404(Guest), many=True)
    # getting students list
    studentSerialized = StudentSerializer(get_list_or_404(Student), many=True)
    # getting lecturers list
    lecturersSerialized = LecturerSerializer(get_list_or_404(Lecturer), many=True)
    # getting registrars list
    registrarsSerialized = RegistrarSerializer(get_list_or_404(Registrar), many=True)
    return Response(registrarsSerialized.data + lecturersSerialized.data + studentSerialized.data + guestsSerialized.data)
