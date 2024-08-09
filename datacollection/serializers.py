from rest_framework import serializers


class PresignedKeySerializer(serializers.Serializer):
    key = serializers.CharField(max_length=255)
    url = serializers.URLField()

class PresignedUploadSerializer(serializers.Serializer):
    presigned_upload_url = serializers.ListField(child=PresignedKeySerializer())
    
class FileMetadataSerializer(serializers.Serializer):
    file_name = serializers.CharField(max_length=255)
    file_type = serializers.ChoiceField(choices=["image/jpeg", "image/png", "image/jpg", "application/pdf"])

class UploadSerializer(serializers.Serializer):
    uploads_filename  = serializers.ListField(child=FileMetadataSerializer())