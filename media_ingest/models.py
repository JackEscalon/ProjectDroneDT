from django.db import models
from cases.models import Case
import cv2


class MediaFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='media_files')

    def __str__(self):
        return f"MediaFile {self.id}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        file_path = self.file.path

        print("\n=== ANALIZA OBRAZU ===")
        print("Plik:", file_path)

        img = cv2.imread(file_path)

        if img is None:
            print("❌ Nie udało się wczytać obrazu")
            return

        print("✅ Obraz wczytany")

        height, width, channels = img.shape
        print(f"Rozdzielczość: {width}x{height}")
        print(f"Kanały: {channels}")