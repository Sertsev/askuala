from rest_framework import serializers

from programs.serializers import BatchSerializer, ProgramSerializer
from .models import *


class RegistrarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registrar
        fields = ['registrarId', 'firstName', 'middleName',
                    'lastName', 'gender', 'email',
                    'phoneNumber', 'birthdate', 'citizenship',
                    'country', 'city', 'educationLevel', 
                    'educationDepartment', 'createdAt', 'lastUpdate']

    def create(self, validated_data):
        registrar = Registrar(**validated_data)
        registrar.password = 'encrypted'
        return super().create(validated_data)


class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ['lecturerId', 'firstName', 'middleName',
                    'lastName', 'gender', 'email', #'documentLocation',
                    'phoneNumber', 'birthdate', 'citizenship',
                    'country', 'city', 'educationLevel',
                    'educationDepartment', 'createdAt', 'lastUpdate']

    def create(self, validated_data):
        lecturer = Lecturer(**validated_data)
        lecturer.password = 'encrypted'
        return super().create(validated_data)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['studentId', 'firstName', 'middleName', 'batch',
                    'lastName', 'gender', 'email', #'documentLocation',
                    'phoneNumber', 'birthdate', 'citizenship', 'currentSemester',
                    'country', 'city', 'program', 'previousEducationLevel',
                    'previousEducationDepartment', 'createdAt', 'lastUpdate', 'verified']
    
    program = ProgramSerializer()
    batch = BatchSerializer()


class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['studentId', 'firstName', 'middleName', 'batch',
                    'lastName', 'gender', 'email', #'documentLocation',
                    'phoneNumber', 'birthdate', 'citizenship', 'currentSemester',
                    'country', 'city', 'program', 'previousEducationLevel',
                    'previousEducationDepartment', 'createdAt', 'lastUpdate', 'verified']

    def create(self, validated_data):
        student = Student(**validated_data)
        student.password = 'encrypted'
        student.save()
        return student


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['guestId', 'firstName', 'middleName',
                    'lastName', 'gender', 'email', #'documentLocation',
                    'phoneNumber', 'birthdate', 'citizenship',
                    'country', 'city', 'educationLevel',
                    'educationDepartment', 'createdAt', 'lastUpdate']

    def create(self, validated_data):
        guest = Guest(**validated_data)
        guest.password = 'encrypted'
        return super().create(validated_data)

