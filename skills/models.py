from django.db import models

class Skill(models.Model):
  title = models.CharField("Название", max_length=250)
  icon = models.ImageField(upload_to="images/skills")

  class Meta:
    verbose_name = "Навыки"
    verbose_name_plural = "Навыки"

  def __str__(self):
    return self.title
