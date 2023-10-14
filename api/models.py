from django.db import models


class File(models.Model):
    """Модель загружаемого файла"""
    file = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('uploaded_at',)
