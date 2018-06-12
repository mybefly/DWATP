__author__ = "zhaichuang"
from rest_framework import serializers

#======上面为第三方包,下面为项目的包=======

from .models import *



class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectInfo()
        fields = "__all__"