"""DWATP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path,include
import xadmin
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
#=======================
from apitest.views import ProjectViewset
from apitest.views import ApiViewSet
from apitest.views import VersionViewSet
from apitest.views import TestCaseViewSet
from apitest.views import StepsViewSet
#=======================
router = DefaultRouter()
router.register('projects',viewset=ProjectViewset,base_name="project_list")
router.register('apis',viewset=ApiViewSet,base_name="api_list")
router.register('versions',viewset=VersionViewSet,base_name="version_list")
router.register('testcases',viewset=TestCaseViewSet,base_name="testcase_list")
router.register('steps',viewset=StepsViewSet,base_name="steps_list")
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('docs',include_docs_urls(title="自动化测试",public=False)),
    path('',include(router.urls))
]
