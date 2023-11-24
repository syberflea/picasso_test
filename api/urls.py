from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r'upload', views.FileUploadViewSet, basename="upload")
router.register(r'files', views.FileListViewSet, basename="files")

urlpatterns = [
    path('', include(router.urls)),
]
