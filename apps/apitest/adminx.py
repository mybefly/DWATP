__author__ = "zhaichuang"
import xadmin
from .models import *
xadmin.site.register(Version)
xadmin.site.register(ProjectInfo)
xadmin.site.register(ApiInfo)
xadmin.site.register(TestCaseInfo)
xadmin.site.register(Steps)
