from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser

from django_filters.rest_framework import DjangoFilterBackend

from school_users.permissions import IsRegistrar

from .serializers import *
from .models import *



# Create your views here.
class AllAssessmentViewSet(ModelViewSet):
    queryset = AllAssessment.objects.all()
    serializer_class = AllAssessmentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['course_id']
    search_fields = ['assignmentTitle']
    permission_classes = [IsAdminUser, IsRegistrar]
