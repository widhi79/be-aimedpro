import uuid
import os

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.core.files.base import ContentFile


class TextToSpeech(ViewSet):
    @action(methods=["post"], detail=True)
    def generate_elevenlabs_voice(self, request):
        try:
            audio_file = request.data.get("audio_file")

            if not audio_file:
                return Response(
                    {"error": "Voice file is required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Generate a unique filename
            uid = str(uuid.uuid4())
            filename = f"voice-{uid}.mp3"

            # Save the file to the media directory
            file_path = os.path.join("D:\\project\\aimed\\assets", filename)
            # with open(f"assets/{filename}", "wb") as destination:
            with open(file_path, "wb") as destination:
                for chunk in audio_file.chunks():
                    destination.write(chunk)

            # You can save additional information to the database or perform other actions here

            return Response(
                {"message": "Voice File Created successfully", "data": filename},
                status=status.HTTP_201_CREATED,
            )

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
