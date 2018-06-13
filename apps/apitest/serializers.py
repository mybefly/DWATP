__author__ = "zhaichuang"
from rest_framework import serializers

#======上面为第三方包,下面为项目的包=======

from .models import *



class ProjectSerializer(serializers.ModelSerializer):
    pname = serializers.CharField(max_length=100)
    class Meta:
        model = ProjectInfo
        fields = "__all__"


    def validate_pname(self, pname):
          if ProjectInfo.objects.filter(pname=pname):
              raise serializers.ValidationError("项目名称已存在")



