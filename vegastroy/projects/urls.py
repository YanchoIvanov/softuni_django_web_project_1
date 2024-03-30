from django.urls import path
from vegastroy.projects.views import project_index, project_detail
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", project_index, name="project_index"),
    path("<int:pk>/", project_detail, name="project_detail"),
]
