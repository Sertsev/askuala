from rest_framework import serializers

from programs.serializers import ProgramSerializer
from .models import *


class RegistrarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registrar
        fields = ['registrarId', 'firstName', 'middleName',
                    'lastName', 'gender', 'email',
                    'phoneNumber', 'birthdate', 'citizenship',
                    'country', 'city', 'educationLevel', 
                    'educationDepartment', 'createdAt', 'lastUpdate']


class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ['lecturerId', 'firstName', 'middleName',
                    'lastName', 'gender', 'email', #'documentLocation',
                    'phoneNumber', 'birthdate', 'citizenship',
                    'country', 'city', 'educationLevel',
                    'educationDepartment', 'createdAt', 'lastUpdate']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['studentId', 'firstName', 'middleName', 'batch',
                    'lastName', 'gender', 'email', #'documentLocation',
                    'phoneNumber', 'birthdate', 'citizenship', 'currentSemester',
                    'country', 'city', 'program', 'previousEducationLevel',
                    'previousEducationDepartment', 'createdAt', 'lastUpdate', 'verified']
    
    program = ProgramSerializer()

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['guestId', 'firstName', 'middleName',
                    'lastName', 'gender', 'email', #'documentLocation',
                    'phoneNumber', 'birthdate', 'citizenship',
                    'country', 'city', 'educationLevel',
                    'educationDepartment', 'createdAt', 'lastUpdate']
