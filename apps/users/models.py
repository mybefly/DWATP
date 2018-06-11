from django.db import models
from django.db import models  #Django的model
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    '''
    用户信息
    '''
    username = models.CharField("用户名",max_length=30,unique=True)
    password = models.CharField("密码",max_length=100)
    email =  models.EmailField("邮箱",max_length=100)
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username