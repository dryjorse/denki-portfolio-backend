from modeltranslation.translator import register, TranslationOptions
from .models import Specialization

@register(Specialization)
class SpecializationTranslationOptions(TranslationOptions):
  fields = ('title',)