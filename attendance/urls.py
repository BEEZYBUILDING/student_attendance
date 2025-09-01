from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, ClassroomViewSet, AttendanceRecordViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'classrooms', ClassroomViewSet)
router.register(r'attendancerecords', AttendanceRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
