from django.db import models
from skills.models import Skill

class Specialization(models.Model):
  title = models.CharField("Название", max_length=250)
  icon = models.ImageField(upload_to="images/specializations")
  skills = models.ManyToManyField(Skill)

  class Meta:
    verbose_name = "Специализации"
    verbose_name_plural = "Специализации"

  def __str__(self):
    return self.title


