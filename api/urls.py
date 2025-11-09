from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import viewsets

router = DefaultRouter()
router.register(r'problems', viewsets.ProblemViewSet)
router.register(r'solutions', viewsets.SolutionViewSet)
router.register(r'tags', viewsets.TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]