from rest_framework import serializers
from .models import *


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ['batchId', 'batchName', 'batchProgram',
                    'batchEntryYear', 'batchGraduationYear']


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Program
        fields = ['programId', 'programName', 'programDescription',
                    'programInfoLink']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['departmentId', 'departmentName', 'departmentDescription',
                    'departmentHead']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['courseId', 'courseName', 'courseDescription',
                    'department']

    department = DepartmentSerializer()


class CiBSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses_in_Batch
        fields = ['id', 'batch', 'program', 'department', 'year', 
                    'semester', 'course', 'courseStarts', 'endCourse']

    batch = BatchSerializer()
    program = ProgramSerializer()
    department = DepartmentSerializer()
    course = CourseSerializer()


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'lessonName', 'lessonDescription', 'course']

    course = CourseSerializer()
