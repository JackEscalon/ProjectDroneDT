from django.db import models
from cases.models import Case

class MediaFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='media_files')

    def __str__(self):
        return f"MediaFile {self.id}"