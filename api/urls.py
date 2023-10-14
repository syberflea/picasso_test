from django.urls import include, path

from .views import upload_file


urlpatterns = [
    path('upload/', upload_file),
]
