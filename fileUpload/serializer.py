from rest_framework import serializers
from fileUpload import models


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FilesModel
        fields = '__all__'
