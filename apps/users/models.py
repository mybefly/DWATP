from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(verbose_name="用户名称",max_length=50)
    email = models.CharField(max_length=50,verbose_name="邮箱")
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name