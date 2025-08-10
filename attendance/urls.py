#NEW
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, ClassroomViewSet

router = DefaultRouter()
router.register(r'Students', StudentViewSet)
router.register(r'Classroom', ClassroomViewSet)

urlpatterns = [
    path('', include(router.urls)),
]