
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from taskapp.api import views



router = routers.DefaultRouter()
router.register('team', views.TeamViewSet, basename='team')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/task/<int:pk>/', views.TaskViewSet.as_view()),
    path('api/v1/task/', views.TaskViewSet.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
