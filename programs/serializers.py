from rest_framework import serializers
from django.conf import settings
from askuala.serializers import UserSerializer
from .models import *



# Batches json input or output extractor
class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ['batchId', 'batchName', 'batchProgram',
                    'batchEntryYear', 'batchGraduationYear',
                    'createdAt', 'lastUpdate']


class SimpleBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ['batchId', 'batchName', 'batchProgram',]


# Degree Programs Json input or output extractor
class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Program
        fields = ['programId', 'programName', 'programDescription',
                  'programInfoLink', 'createdAt', 'lastUpdate']


class SimpleProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Program
        fields = ['programId', 'programName', 'programDescription']


# Departments json input or output extractor
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['departmentId', 'departmentName', 'departmentDescription',
                  'departmentHead', 'createdAt', 'lastUpdate']


class SimpleDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['departmentId', 'departmentName', 'departmentDescription',]


# Courses json input or output extractor
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['courseId', 'courseName', 'courseDescription',
                  'department', 'createdAt', 'lastUpdate']

    department = SimpleDepartmentSerializer()


class SimpleCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['courseId', 'courseName', 'courseDescription']


# Courses in Batch json input or output extractor
class CiBSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses_in_Batch
        fields = ['id', 'batch', 'program', 'department', 'year', 
                    'semester', 'course', 'courseStarts', 'endCourse', 
                    'createdAt', 'lastUpdate']

    batch = BatchSerializer()
    program = ProgramSerializer()
    department = DepartmentSerializer()
    course = CourseSerializer()


class SimpleCiBSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses_in_Batch
        fields = ['id', 'batch', 'program', 'department', 'year',
                    'semester', 'course', 'courseStarts', 'endCourse',
                    'createdAt', 'lastUpdate']
    course = SimpleCourseSerializer()


# Lessons json input or output extractor
class LessonSerializer(serializers.ModelSerializer):
    lecturer = UserSerializer(read_only=True)
    embedVideo = serializers.CharField(read_only=True)
    resources = serializers.CharField(read_only=True)
    class Meta:
        model = Lesson
        fields = ['id', 'lessonTitle', 'lessonDescription',
                    'course', 'resources', 'lecturer', 'embedVideo',
                    'createdAt', 'lastUpdate']

    course = CourseSerializer()


class LessonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'lessonTitle', 'lessonDescription',
                  'course', 'resources', 'lecturer', 'embedVideo',
                  'createdAt', 'lastUpdate']


# handling enrollment applications
class StudentApplicationsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    # guest = settings.GUEST_SERIALIZER(read_only=True)
    class Meta:
        model = StudentApplications
        fields = ['user', 'guest', 'batch', 'program', 'department', 'enrollment_type', 
                    'createdAt', 'lastUpdate']