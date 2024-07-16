from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CoachViewSet, LessonViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'coaches', CoachViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
