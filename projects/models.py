from django.db import models
from skills.models import Skill
from specializations.models import Specialization

class Project(models.Model):
  title = models.CharField("Название", max_length=250)
  date = models.DateField("Дата завершения")
  description = models.TextField("Описание")
  image = models.ImageField(upload_to="images/projects")
  order = models.IntegerField("Место", default=1)
  skills = models.ManyToManyField(Skill)
  specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True)

  class Meta:
    verbose_name = "Проекты"
    verbose_name_plural = "Проекты"

  def __str__(self):
    return self.title