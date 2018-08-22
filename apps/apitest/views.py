from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
#==================================
from .models import *
from .serializers import ProjectSerializer
from .serializers import ApiSerializer
from .serializers import VersionSerializer
from .serializers import TestCaseSerializer
from .serializers import StepsSerializer
from utils.api_response import response

# Create your views here.

class pages(PageNumberPagination):
    page_size = 10
    page_query_param = "page"

class ProjectViewset(viewsets.ModelViewSet,generics.GenericAPIView):
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
    pagination_class = pages

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset, many=True)
        if self.paginate_queryset(self.queryset) is not None:
            serializer = self.get_serializer(self.paginate_queryset(self.queryset), many=True)
            return self.get_paginated_response(serializer.data)
        return response(data=serializer.data,code=0,msg="ok")

class ApiViewSet(viewsets.ModelViewSet,generics.GenericAPIView):
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
    responsedata ={}
    queryset = ApiInfo.objects.all()
    serializer_class = (ApiSerializer)
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        # page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(queryset, many=True)
        return response(data=serializer.data,code=0,msg="ok")



        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     self.responsedata["code"]=1000
        #     self.responsedata["msg"]="ok"
        #     self.responsedata["data"]=serializer.data
        #     return self.get_paginated_response(self.responsedata)
        # serializer = self.get_serializer(queryset, many=True)
        # self.responsedata["code"]=1000
        # self.responsedata["msg"]="ok"
        # self.responsedata["data"]=serializer.data
        # return Response(self.responsedata)
        # return response(data=serializer.data,code=0,msg="ok")

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if not serializer.data:
           self.responsedata["code"]=404
           self.responsedata["msg"]="无信息"
           self.responsedata["data"]=serializer.data
           return Response(self.responsedata)
        return Response(self.responsedata)

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
    pagination_class = pages
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            self.get_paginated_response(serializer.data)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return response(data=serializer.data,code=0,msg='ok')

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












