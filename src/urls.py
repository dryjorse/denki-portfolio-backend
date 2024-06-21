from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.routers import SimpleRouter
from skills.views import SkillsView
from specializations.views import SpecializationsView
from projects.views import ProjectsView


router = SimpleRouter()

router.register('skills', SkillsView)
router.register('specializations', SpecializationsView)
router.register('projects', ProjectsView)

urlpatterns = [
    path('admin/', admin.site.urls),    
    path("api/", include(router.urls))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()