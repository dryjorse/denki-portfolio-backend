from rest_framework.viewsets import ModelViewSet
from .models import Skill
from .serializers import SkillSerializer

class SkillsView(ModelViewSet):
  queryset = Skill.objects.all()
  serializer_class = SkillSerializer

