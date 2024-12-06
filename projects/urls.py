from django.urls import path
from rest_framework import routers
from .api import ProjectViewSet
from . import views

router = routers.DefaultRouter()
router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = [
    path('index.html', views.index, name='index'),
    path('projects/', views.project_list, name='project-list'),
] + router.urls