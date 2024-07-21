from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, LessonViewSet, BookingViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
