#NEW
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, ClassroomViewSet, AttendanceRecordViewSet

router = DefaultRouter()
router.register(r'Students', StudentViewSet)
router.register(r'Classroom', ClassroomViewSet)
router.register(r'AttendanceRecord', AttendanceRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]