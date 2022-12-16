from rest_framework import serializers
from programs.serializers import SimpleBatchSerializer, SimpleProgramSerializer, SimpleDepartmentSerializer, CourseSerializer
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
    currentYear = serializers.IntegerField(read_only=True)
    currentSemester = serializers.IntegerField(read_only=True)
    enrollment_type = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = ['studentId',  'user', 'birthdate', 
                    'citizenship', 'currentCountry', 'city', 'address',
                    'batch', 'currentYear', 'currentSemester', 'enrolledProgram', 'enrolledDepartment',
                    'educationLevel', 'educationDepartment', 'enrollment_type',
                    'createdAt', 'lastUpdate']


class SimpleStudentSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer(read_only=True)
    enrolledProgram = SimpleProgramSerializer(read_only=True)
    enrolledDepartment = SimpleDepartmentSerializer(read_only=True)
    batch = SimpleBatchSerializer(read_only=True)
    currentYear = serializers.IntegerField(read_only=True)
    currentSemester = serializers.IntegerField(read_only=True)

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

    def save(self, **kwargs):
        return super().save(**kwargs)

    def create(self, validated_data):
        user_d = User(**validated_data)
        path = str(BASE_DIR) + '\\media\\users\\' + user_d.username + '\\'
        if os.path.exists(str(BASE_DIR) + '\\media'):
            if not os.path.exists(path):
                os.makedirs(path)
                print("User Directory '% s' created." % path)
        return super().create(validated_data)


class ACserializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    lecturer = SimpleLecturerSerializer(read_only=True)
    department = SimpleDepartmentSerializer(read_only=True)
    registrar = SimpleUserSerializer(read_only=True)

    class Meta:
        model = AssignCourses
        fields = ['id', 'course', 'lecturer', 'department', 'registrar', 'course_type',
                    'createdAt', 'lastUpdate']


class ACcreateSerializer(serializers.ModelSerializer):
    registrar = SimpleUserSerializer(read_only=True)
    class Meta:
        model = AssignCourses
        fields = ['id', 'course', 'lecturer', 'department', 'registrar', 'course_type',
                    'createdAt', 'lastUpdate']


class AClecturerSerializer(serializers.ModelSerializer):
    registrar = SimpleUserSerializer(read_only=True)
    course = CourseSerializer(read_only=True)
    registrar = SimpleUserSerializer(read_only=True)
    class Meta:
        model = AssignCourses
        fields = ['id', 'course', 'lecturer', 'department', 'registrar', 'course_type',
                    'createdAt', 'lastUpdate']
