from celery import shared_task
from django.shortcuts import get_object_or_404

from api.models import File


@shared_task
def create_task(data):
    file = get_object_or_404(File, id=data.id)
    if file:
        file.processed = True
        file.save()
        return True
    return False
