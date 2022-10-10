from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Batch view handlers
@api_view()
def all_batches(request):
    queryset = get_list_or_404(Batch)
    serialized =  BatchSerializer(queryset, many=True)
    return Response(serialized.data)


@api_view()
def batch_info(request, pk):
    batch = get_object_or_404(Batch, pk=pk)
    serialized = BatchSerializer(batch)
    return Response(serialized.data)


# Degree or Program view handlers
@api_view()
def all_degrees(request):
    queryset = get_list_or_404(Program)
    serialized = ProgramSerializer(queryset, many=True)
    return Response(serialized.data)


@api_view()
def degree_info(request, pk):
    degree = get_object_or_404(Program, pk=pk)
    serialized = ProgramSerializer(degree)
    return Response(serialized.data)


# Department view handlers
@api_view()
def all_departments(request):
    queryset = get_list_or_404(Department)
    serialized = DepartmentSerializer(queryset, many=True)
    return Response(serialized.data)


@api_view()
def department_info(request, pk):
    dep = get_object_or_404(Department, pk=pk)
    serialized = DepartmentSerializer(dep)
    return Response(serialized.data)


# Course view handlers
@api_view()
def all_courses(request):
    queryset = Course.objects.select_related('department').all()
    serialized = CourseSerializer(queryset, many=True)
    return Response(serialized.data)


@api_view()
def course_info(request, pk):
    course = get_object_or_404(Course, pk=pk)
    serialized = CourseSerializer(course)
    return Response(serialized.data)


# Course in batch view handlers
@api_view()
def all_cib(request):
    queryset = Courses_in_Batch.objects.select_related('batch', 'program', 'department', 'course').all()
    serialized = CiBSerializer(queryset, many=True)
    return Response(serialized.data)


@api_view()
def cib_info(request, pk):
    cib = get_object_or_404(Courses_in_Batch, pk=pk)
    serialized = CiBSerializer(cib)
    return Response(serialized.data)


# Lesson view handlers
@api_view()
def all_lessons(request):
    queryset = Lesson.objects.select_related('course').all()
    serialized = LessonSerializer(queryset, many=True)
    return Response(serialized.data)


@api_view()
def lesson_info(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    serialized = LessonSerializer(lesson)
    return Response(serialized.data)
