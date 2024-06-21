from rest_framework import serializers
from .models import Specialization
from skills.serializers import SkillSerializer

class SpecializationSerializer(serializers.ModelSerializer):
  skills = SkillSerializer(many=True, read_only=True)

  class Meta:
    model = Specialization
    fields = "__all__"  
    