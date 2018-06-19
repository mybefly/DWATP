__author__ = "zhaichuang"
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
#======上面为第三方包,下面为项目的包=======
from django.contrib.auth import get_user_model

User = get_user_model()

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ["id","username","email"]


#项目信息Serializer
class ProjectSerializer(serializers.ModelSerializer):
    pname = serializers.CharField(required=True,max_length=100,validators=[UniqueValidator(queryset=ProjectInfo.objects.all(),message="项目已存在")])
    pdesc = serializers.CharField(allow_blank=True)
    add_time=serializers.DateField(allow_null=True)
    update_time = serializers.DateField(allow_null=True)
    cuser = UserSerializer(read_only=True)
    update_user = UserSerializer(read_only=True)
    class Meta:
        model = ProjectInfo
        fields = "__all__"


#接口信息Serializer
class ApiSerializer(serializers.ModelSerializer):
    aname = serializers.CharField(max_length=100,validators=[UniqueValidator(queryset=ApiInfo.objects.all(),message="接口名称已存在"),])
    apath = serializers.CharField(max_length=50,validators=[UniqueValidator(queryset=ApiInfo.objects.all(),message="接口路径已存在"),])
    add_time=serializers.DateField(allow_null=True)
    update_time = serializers.DateField(allow_null=True)
    cuser = UserSerializer(read_only=True)
    update_user = UserSerializer(read_only=True)

    class Meta:
        model = ApiInfo
        fields = "__all__"


#版本号Serializer:
class VersionSerializer(serializers.ModelSerializer):
    version = serializers.CharField(max_length=30,validators=[UniqueValidator(queryset=Version.objects.all(),message="版本号已存在")])
    class Meta:
        model = Version
        fields = "__all__"



#测试用例Serializer:
class TestCaseSerializer(serializers.ModelSerializer):
    tname = serializers.CharField(max_length=50,validators=[UniqueValidator(queryset=TestCaseInfo.objects.all(),message="用例已存在")])
    add_time=serializers.DateField(allow_null=True)
    update_time = serializers.DateField(allow_null=True)
    cuser = UserSerializer(read_only=True)
    update_user = UserSerializer(read_only=True)
    class Meta:
        model = TestCaseInfo
        fields = "__all__"


#测试步骤Serializer
class StepsSerializer(serializers.ModelSerializer):
    sname = serializers.CharField(max_length=50,validators=[UniqueValidator(queryset=Steps.objects.all(),message="用例已存在")])
    add_time=serializers.DateField(allow_null=True)
    class Meta:
        model = Steps
        fields = "__all__"
