from rest_framework import serializers
from .models import Project
from skills.serializers import SkillSerializer

class ProjectSerializer(serializers.ModelSerializer):
  skills = SkillSerializer(many=True, read_only=True)

  class Meta:
    model = Project
    fields = "__all__"  
    