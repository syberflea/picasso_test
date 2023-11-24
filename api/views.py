from rest_framework import mixins, viewsets

from api.models import File
from api.serializers import FileSerializer


class FileUploadViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    This viewset automatically provides `create`.
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer


class FileListViewSet(mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    """
    This viewset automatically provides `list`.
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer
