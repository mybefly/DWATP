from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
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
    serializer_class = (ProjectSerializer)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pname = serializer.validated_data["pname"]
        try:
            project = ProjectInfo(pname=pname,pdesc="测试")
            project.save()
            return Response(project,status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)












