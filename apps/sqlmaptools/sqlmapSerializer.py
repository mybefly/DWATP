__author__ = "zhaichuang"

from rest_framework import serializers
from sqlmaptools.models import URLInfo

class sqlmapApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLInfo
        fields = "__all__"