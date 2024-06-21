from rest_framework.viewsets import ModelViewSet
from .models import Specialization
from .serializers import SpecializationSerializer

class SpecializationsView(ModelViewSet):
  queryset = Specialization.objects.all()
  serializer_class = SpecializationSerializer

