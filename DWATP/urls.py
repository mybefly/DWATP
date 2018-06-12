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
#=======================
router = DefaultRouter()
router.register('projects',viewset=ProjectViewset,base_name="project_list")
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('docs',include_docs_urls("rest_framework.urls")),
    path('',include(router.urls))

]
