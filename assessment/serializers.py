from rest_framework.serializers import ModelSerializer
from programs.serializers import SimpleBatchSerializer, SimpleDepartmentSerializer, SimpleCourseSerializer
from school_users.serializers import *
from .models import *


class AssignmentSerializer(ModelSerializer):
    lecturer = SimpleLecturerSerializer(read_only=True)
    course = SimpleCourseSerializer(read_only=True)
    class Meta:
        model = Assignment
        fields = ['assignmentId', 'assignmentTitle',
                    'assignmentDescription', 'maxPoint', 'lecturer', 'course', 
                    'fileLocation', 'createdAt', 'lastUpdate', 'active']


class SimpleAssignmentSerializer(ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['assignmentId', 'assignmentTitle', 'maxPoint', 'lecturer', 'course',
                    'active']

class GivenAssignmentSerializer(ModelSerializer):
    batch = SimpleBatchSerializer(read_only=True)
    department = SimpleDepartmentSerializer(read_only=True)
    assignment = SimpleAssignmentSerializer()

    class Meta:
        model = Assignment
        fields = ['assignment', 'batch', 'department', 'deadline', 
                    'createdAt', 'lastUpdate', 'active']


class AssignmentPointSerializer(ModelSerializer):
    student = SimpleStudentSerializer(read_only=True)
    assignment = SimpleAssignmentSerializer(read_only=True)
    class Meta:
        model = AssignmentPoint
        fields = ['student', 'assignment', 'point', 'maxPoint', 'feedback',
                    'createdAt', 'lastUpdate']


class QuizSerializer(ModelSerializer):
    lecturer = SimpleLecturerSerializer(read_only=True)
    course = SimpleCourseSerializer(read_only=True)
    class Meta:
        model = Quiz
        fields = ['quizId', 'quizTitle', 'quizDescription', 'maxPoint', 'givenTime',
                    'lecturer', 'course', 'fileLocation', 'createdAt', 'lastUpdate', 'active']


class SimpleQuizSerializer(ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['quizId', 'quizTitle', 'maxPoint', 'givenTime',
                    'lecturer', 'course', 'active']


class GivenQuizSerializer(ModelSerializer):
    quiz = SimpleQuizSerializer(read_only=True)
    batch = SimpleBatchSerializer(read_only=True)
    class Meta:
        model = GivenQuiz
        fields = ['quiz', 'batch', 'department', 'openingTime', 'clothingTime',
                    'createdAt', 'lastUpdate', 'active']


class QuizQuestionSerializer(ModelSerializer):
    quiz = SimpleQuizSerializer(read_only=True)
    class Meta:
        model = QuizQuestion
        fields = ['quiz', 'questionTitle', 'questionDetail', 'fileLocation', 
                    'choiceA', 'choiceB', 'choiceC', 'choiceD', 'choiceE', 'choiceF', 'choiceG',
                    'answer', 'givenTime', 'maxPoint', 'createdAt', 'lastUpdate']


class QuizPointSerializer(ModelSerializer):
    student = SimpleStudentSerializer(read_only=True)
    quiz = SimpleQuizSerializer(read_only=True)
    class Meta:
        model = QuizPoint
        fields = ['student', 'quiz', 'point', 'maxPoint', 'feedback',
                    'createdAt', 'lastUpdate']


class AllAssessmentSerializer():
    student = SimpleStudentSerializer(read_only=True)
    course = SimpleCourseSerializer(read_only=True)
    class Meta:
        model = AllAssessment
        fields = ['student', 'course', 'assignmentOnePoint', 'assignmentTwoPoint',
                    'quizPoint', 'midExamPoint', 'finalExamPoint', 'total', 'grade'
                    'createdAt', 'lastUpdate']
