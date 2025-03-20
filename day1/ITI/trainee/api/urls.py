from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TraineeViewSet

router = DefaultRouter()
router.register(r'trainees', TraineeViewSet, basename="trainee")

urlpatterns = [
    path('', include(router.urls)),
]
