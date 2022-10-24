from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

"""
    Here under all the get requests of all the users handled here
        anybody with an id or 's url can get results from the 
        following functions
"""

#  Registrar users api view handler
class RegistrarViewSet(ModelViewSet):
    queryset = Registrar.objects.all()
    serializer_class = RegistrarSerializer


#  Lecturer users api view handlers
@api_view(['GET', 'POST'])
def lecturers_list(request):
    if request.method == 'GET':
        queryset = get_list_or_404(Lecturer)
        serializer = LecturerSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serialized = LecturerSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response(serialized.validated_data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PATCH', 'DELETE'])
def lecturer_info(request, id):
    lecturer = get_object_or_404(Lecturer, pk=id)
    if request.method == 'GET':
        serializer = LecturerSerializer(lecturer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serialized = LecturerSerializer(lecturer, data=request.data, partial=True)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response(serialized.data)
    elif request.method == 'DELETE':
        lecturer.delete()
        return Response({"Success": f"The lecturer with an ID-{id} is successfully deleted."}, status.HTTP_204_NO_CONTENT)


#  Student users api view handler
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['batch_id', 'program_id']
    search_fields = ['firstName', 'middleName', 'lastName']


# @api_view(['GET', 'POST'])
# def students_list(request):
#     if request.method == 'GET':
#         queryset = Student.objects.select_related('program', 'batch').all()
#         serializer = StudentSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serialized = StudentRegisterSerializer(data=request.data)
#         serialized.is_valid(raise_exception=True)
#         serialized.save()
#         return Response(serialized.validated_data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PATCH', 'DELETE'])
# def student_info(request, id):
#     student = get_object_or_404(Student, pk=id)
#     if request.method == 'GET':
#         serializer = StudentSerializer(student)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PATCH':
#         serialized = StudentRegisterSerializer(student, data=request.data, partial=True)
#         serialized.is_valid(raise_exception=True)
#         serialized.save()
#         return Response(serialized.data)
#     elif request.method == 'DELETE':
#         student.delete()
#         return Response({"Success": f"The student with an ID-{id} is successfully deleted."}, status.HTTP_204_NO_CONTENT)



#  Guest users api view handlers
@api_view(['GET', 'POST'])
def guests_list(request):
    if request.method == 'GET':
        queryset = get_list_or_404(Guest)
        serializer = GuestSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serialized = GuestSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response(serialized.validated_data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PATCH', 'DELETE'])
def guest_info(request, id):
    guest = get_object_or_404(Guest, pk=id)
    if request.method == 'GET':
        serializer = GuestSerializer(guest)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serialized = GuestSerializer(guest, data=request.data, partial=True)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response(serialized.data)
    elif request.method == 'DELETE':
        guest.delete()
        return Response({"Success": f"The guest with an ID-{id} is successfully deleted."}, status.HTTP_204_NO_CONTENT)


# To see all users
@api_view()
def all_users(request):
    # getting guests list
    guestsSerialized = GuestSerializer(get_list_or_404(Guest), many=True)
    # getting students list
    studentSerialized = StudentSerializer(get_list_or_404(Student.objects.select_related('program', 'batch')), many=True)
    # getting lecturers list
    lecturersSerialized = LecturerSerializer(get_list_or_404(Lecturer), many=True)
    # getting registrars list
    registrarsSerialized = RegistrarSerializer(get_list_or_404(Registrar), many=True)
    return Response(registrarsSerialized.data + lecturersSerialized.data + studentSerialized.data + guestsSerialized.data, status=status.HTTP_200_OK)
