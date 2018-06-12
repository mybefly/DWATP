from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
#==================================
from .models import *
from .serializers import ProjectSerializer
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
    serializer_class = ProjectSerializer











