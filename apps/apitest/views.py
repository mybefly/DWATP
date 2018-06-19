from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
#==================================
from .models import *
from .serializers import ProjectSerializer
from .serializers import ApiSerializer
from .serializers import VersionSerializer
from .serializers import TestCaseSerializer
from .serializers import StepsSerializer
# Create your views here.

class ProjectViewset(viewsets.GenericViewSet,mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    '''
    list:
        获取项目信息列表
    retrieve:
        获取项目详情
    create:
        创建项目
    update:
        更新项目信息
    destroy:
        删除项目
    '''
    queryset = ProjectInfo.objects.all()
    serializer_class = (ProjectSerializer)

class ApiViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,
                 mixins.CreateModelMixin):

    '''
    list:
        获取接口信息列表
    retrieve:
        获取项目详情
    create:
        添加接口
    update:
        更新接口信息
    destroy:
        删除接口
    '''
    queryset = ApiInfo.objects.all()
    serializer_class = (ApiSerializer)
class TestCaseViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin):
    '''
    list:
        获取接口信息列表
    retrieve:
        获取项目详情
    create:
        添加接口
    update:
        更新接口信息
    destroy:
        删除接口
    '''
    queryset = TestCaseInfo.objects.all()
    serializer_class = (TestCaseSerializer)
class VersionViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin):
    '''
    list:
        获取版本信息
    retrieve:
        获取版本详情
    create:
        添加版本
    update:
        更新版本信息
    destroy:
        删除版本
    '''
    queryset = Version.objects.all()
    serializer_class = (VersionSerializer)
class StepsViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin):
    '''
    list:
        获取步骤信息
    retrieve:
        获取步骤详情
    create:
        添加步骤
    update:
        更新步骤信息
    destroy:
        删除步骤
    '''
    queryset = Steps.objects.all()
    serializer_class = (StepsSerializer)












