from rest_framework import serializers
from programs.serializers import SimpleBatchSerializer, SimpleProgramSerializer, SimpleDepartmentSerializer, SimpleCourseSerializer
from askuala.serializers import SimpleUserSerializer
from .models import *


# Registrar user json input or output extractor
class RegistrarSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer(read_only=True)
    class Meta:
        model = Registrar
        fields = ['registrarId', 'user', 'birthdate', 
                    'citizenship', 'currentCountry', 'city', 'address',
                    'educationLevel', 'educationDepartment', 
                    'createdAt', 'lastUpdate']


class SimpleRegistrarSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer(read_only=True)

    class Meta:
        model = Registrar
        fields = ['registrarId', 'user']


# Lecturer user json input or output extractor
class LecturerSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer(read_only=True)
    class Meta:
        model = Lecturer
        fields = ['lecturerId', 'user', 'documentLocation',
                    'citizenship', 'currentCountry', 'city', 'address',
                    'educationLevel', 'educationDepartment', 
                    'createdAt', 'lastUpdate']


class SimpleLecturerSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer(read_only=True)

    class Meta:
        model = Lecturer
        fields = ['lecturerId', 'user']


# Student user json input or output extractor
class StudentSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer(read_only=True)
    enrolledProgram = SimpleProgramSerializer(read_only=True)
    enrolledDepartment = SimpleDepartmentSerializer(read_only=True)
    batch = SimpleBatchSerializer(read_only=True)
    class Meta:
        model = Student
        fields = ['studentId',  'user', 'documentLocation', 'birthdate', 
                    'citizenship', 'currentCountry', 'city', 'address',
                    'batch', 'currentYear', 'currentSemester', 'enrolledProgram', 'enrolledDepartment',
                    'educationLevel', 'educationDepartment', 'enrollment_type',
                    'createdAt', 'lastUpdate']


class SimpleStudentSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer(read_only=True)
    enrolledProgram = SimpleProgramSerializer(read_only=True)
    enrolledDepartment = SimpleDepartmentSerializer(read_only=True)
    batch = SimpleBatchSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ['studentId',  'user', 'batch', 'currentYear', 'currentSemester', 
                    'enrolledProgram', 'enrolledDepartment', 'enrollment_type']


# Guest user json input or output extractor
class GuestSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer(read_only=True)
    class Meta:
        model = Guest
        fields = ['guestId', 'user', 'birthdate', 'citizenship',
                    'currentCountry', 'city', 'address', 'educationLevel',
                    'educationDepartment', 'documentLocation', 
                    'createdAt', 'lastUpdate']


class ACserializer(serializers.ModelSerializer):
    # course = SimpleCourseSerializer()
    # lecturer = SimpleLecturerSerializer()
    # batch = SimpleBatchSerializer()
    # department = SimpleDepartmentSerializer()
    registrar = SimpleRegistrarSerializer(read_only=True)
    class Meta:
        model = AssignCourses
        fields = ['id', 'course', 'lecturer', 'batch', 'department', 'registrar', 
                    'createdAt', 'lastUpdate']

