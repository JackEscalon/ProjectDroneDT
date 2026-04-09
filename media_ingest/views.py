from rest_framework import viewsets
from .models import MediaFile
from .serializers import MediaFileSerializer
from .ai import analyze_image


class MediaFileViewSet(viewsets.ModelViewSet):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileSerializer

    def perform_create(self, serializer):
        media_file = serializer.save()

        file_path = media_file.file.path
        label, score, processed_path = analyze_image(file_path)

        print(f"AI: {label} ({score})")
        print(f"Processed image: {processed_path}")