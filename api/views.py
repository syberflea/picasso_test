from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from Picasso_test.tasks import create_task
from api.models import File
from api.serializers import FileSerializer


@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload_file(request):
    file = request.FILES['file']
    file_object = File.objects.create(file=file)
    if create_task(file_object):
        serializer = FileSerializer(file_object, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def file_list(request):
    files = File.objects.all()
    serializer = FileSerializer(files, many=True)
    return Response(serializer.data)
