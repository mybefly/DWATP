from django.db import models
from datetime import datetime #引入时间
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class ProjectInfo(models.Model):
    '''
    项目信息表,存储项目信息
    '''
    pname = models.CharField("项目名称",max_length=100,)
    pdesc = models.CharField('项目描述',max_length=500)
    cuser = models.ForeignKey(User,verbose_name="创建者",null=True,blank=True,on_delete=models.SET_NULL,related_name="cuser")
    update_user = models.ForeignKey(User,verbose_name="更新者",null=True,blank=True,on_delete=models.SET_NULL)
    add_time = models.DateField("添加时间",null=True,blank=True)
    update_time = models.DateField("更新时间",null=True,blank=True)
    class Meta:
        verbose_name = u"项目信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.pname

class Version(models.Model):
    '''
    版本表
    '''
    version = models.CharField("版本",max_length=30)
    add_time = models.DateField("添加时间",null=True,blank=True)
    class Meta:
        verbose_name = "版本信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.version

class ApiInfo(models.Model):
    '''
    接口信息表
    '''
    STAUS=(
        (1,"create"),
        (2,"enable"),
        (2,"update"),
        (3,"disable"),
    )
    aname = models.CharField('接口名称',max_length=100)
    apath = models.CharField('接口路径',max_length=50)
    aheaders = models.CharField("接口Headers信息",max_length=100,null=True,blank=True)
    aparams = models.TextField ("参数内容",max_length=5000)
    aresponse = models.TextField("参数返回")
    astaus = models.IntegerField("接口状态",choices=STAUS)
    aproject = models.ForeignKey(ProjectInfo,verbose_name="所属项目",on_delete=models.CASCADE)
    aversion = models.ForeignKey(Version,verbose_name="接口版本",on_delete=models.SET("1.0.0"))
    cuser = models.ForeignKey(User,verbose_name="创建者",null=True,blank=True,on_delete=models.SET_NULL,related_name="auser")
    pdate_user = models.ForeignKey(User,verbose_name="更新者",null=True,blank=True,on_delete=models.SET_NULL)
    add_time = models.DateField("添加时间",null=True,blank=True)
    update_time = models.DateField("更新时间",null=True,blank=True)
    class Meta:
        verbose_name = "接口信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.aname


class TestCaseInfo(models.Model):
    '''
    测试用例
    '''
    TSTAUS=(
        (1,"PASS"),
        (0,"FAIL"),
        (2,"STOP")
    )
    tname = models.CharField("用例名称",max_length=50)
    tdesc = models.CharField("用例描述",max_length=100,null=True,blank=True)
    tsteps = models.CharField("用例步骤",max_length=100,null=True,blank=True)
    tstaus = models.IntegerField("用例状态",choices=TSTAUS,default=2)
    tproject = models.ForeignKey(ProjectInfo,verbose_name="所属项目",on_delete=models.CASCADE)
    tapi = models.ForeignKey(ApiInfo,verbose_name="所属接口",on_delete=models.CASCADE)
    tversion = models.ForeignKey(Version,verbose_name="测试用例版本",on_delete=models.SET("1.0.0"))
    cuser = models.ForeignKey(User,verbose_name="创建者",null=True,blank=True,on_delete=models.SET_NULL,related_name="tuser")
    update_user = models.ForeignKey(User,verbose_name="更新者",null=True,blank=True,on_delete=models.SET_NULL)
    add_time = models.DateField("添加时间",null=True,blank=True)
    update_time = models.DateField("更新时间",null=True,blank=True)
    class Meta:
        verbose_name = "用例信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.tname

class Steps(models.Model):
    '''
    测试步骤
    '''
    sname = models.CharField("步骤名称",max_length=50)
    spath = models.CharField("接口路径",max_length=50)
    sdata = models.CharField("接口数据",max_length=50)
    stestcase = models.ForeignKey(TestCaseInfo,verbose_name="所属用例",on_delete=models.CASCADE)
    add_time = models.DateField("添加时间",null=True,blank=True)

    class Meta:
        verbose_name = "测试步骤"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.sname