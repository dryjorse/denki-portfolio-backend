from rest_framework.viewsets import ModelViewSet
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class ProjectsView(ModelViewSet):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer
  filter_backends = [OrderingFilter, DjangoFilterBackend]
  filterset_fields = ['specialization']
  ordering_fields = ['date, order']
  ordering = ['-order', 'date']  

