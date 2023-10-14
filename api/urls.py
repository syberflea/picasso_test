from django.urls import include, path

from .views import upload_file, file_list

urlpatterns = [
    path('upload/', upload_file),
    path('files/', file_list),
]
