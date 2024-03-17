from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from moviepy.editor import AudioFileClip, VideoFileClip
from urllib.request import urlopen


class MediaDuration(ViewSet):
    @action(methods=["get"], detail=False)
    def get_media_duration(self, request):
        media_file_url = self.request.query_params.get("media_file_path", "")

        _, file_extension = media_file_url.rsplit(".", 1)

        if file_extension.lower() in ["mp3", "wav"]:
            audioClip = AudioFileClip(media_file_url)
            audioDuration = audioClip.duration
            print(f"Audio Duration: {audioDuration} seconds")
            return Response(
                {
                    "message": "Get Audio Duration Successfull",
                    "duration": audioDuration,
                },
                status=status.HTTP_201_CREATED,
            )

        elif file_extension.lower() in ["mp4", "avi", "mkv"]:
            videoClip = VideoFileClip(media_file_url)
            videoDuration = videoClip.duration
            print(f"Video Duration: {videoDuration} seconds")
            return Response(
                {
                    "message": "Get Video Duration Successfull",
                    "duration": videoDuration,
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response({"message": f"Unsupported file type: {file_extension}"})
