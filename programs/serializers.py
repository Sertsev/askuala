from rest_framework import serializers
from .models import *


# Batches json input or output extractor
class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ['batchId', 'batchName', 'batchProgram',
                    'batchEntryYear', 'batchGraduationYear']


class SimpleBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ['batchId', 'batchName', 'batchProgram',]


# Degree Programs Json input or output extractor
class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Program
        fields = ['programId', 'programName', 'programDescription',
                    'programInfoLink']


class SimpleProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Program
        fields = ['programId', 'programName', 'programDescription']


# Departments json input or output extractor
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['departmentId', 'departmentName', 'departmentDescription',
                    'departmentHead'] 


class SimpleDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['departmentId', 'departmentName', 'departmentDescription',]


# Courses json input or output extractor
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['courseId', 'courseName', 'courseDescription',
                    'department']

    department = DepartmentSerializer()


class SimpleCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['courseId', 'courseName', 'courseDescription']


# Courses in Batch json input or output extractor
class CiBSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses_in_Batch
        fields = ['id', 'batch', 'program', 'department', 'year', 
                    'semester', 'course', 'courseStarts', 'endCourse']

    batch = BatchSerializer()
    program = ProgramSerializer()
    department = DepartmentSerializer()
    course = CourseSerializer()


# Lessons json input or output extractor
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'lessonName', 'lessonDescription', 'course']

    course = CourseSerializer()
