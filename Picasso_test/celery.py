import os
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Picasso_test.settings")
app = Celery("picasso_test")
app.config_from_object("django.conf:settings")
app.autodiscover_tasks(settings.INSTALLED_APPS)
