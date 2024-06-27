from django.contrib import admin
from .models import Project
from modeltranslation.admin import TranslationAdmin

@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
  list_display = ('title', 'date')
  search_fields = ('title', 'description')

  class Media:
    js = (
      'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
      'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
      'modeltranslation/js/tabbed_translation_fields.js',
    )
    css = {
      'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
    }
    

