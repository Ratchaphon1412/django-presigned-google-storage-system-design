from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import time
from django.conf import settings
from .serializers import UploadSerializer, PresignedUploadSerializer
from .service.storage.gcs import generate_upload_signed_url_v4, generate_download_signed_url_v4,generate_signed_url

# Create your views here.
class UploadView(APIView):
    serializer_class = UploadSerializer
    def get(self, request, key):
        # url = generate_download_signed_url_v4(settings.GCP_GCS_BUCKET, key)
        url = generate_signed_url(settings.GCP_GCS_BUCKET, key)
        return Response({"file_url": url}, status=status.HTTP_200_OK)
    def post(self, request):
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                list_url = []
                for file in serializer.data["uploads_filename"]:
                    key = file["file_name"]+"-"+str(int(time.time()))
                    url = generate_upload_signed_url_v4(settings.GCP_GCS_BUCKET, key)
                    list_url.append({"key": key, "url": url})
                response_serializer = PresignedUploadSerializer(data={"presigned_upload_url": list_url})
                if response_serializer.is_valid(raise_exception=True):  
                    return Response(response_serializer.data, status=status.HTTP_200_OK)           
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
