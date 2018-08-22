from django.db import models

# Create your models here.
from apps.apitest.models import ProjectInfo


class URLInfo(models.Model):
    name = models.CharField(max_length=50,verbose_name="接口名称")
    method = models.IntegerField(choices=((1,"GET"),(2,"POST")))
    urlInfo = models.CharField(max_length=100)
    project = models.ForeignKey(ProjectInfo)
    create_time= models.DateField()
    update_time = models.DateField()
