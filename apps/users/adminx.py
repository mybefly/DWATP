__author__ = "zhaichuang"
import xadmin
from xadmin import views #配置全局设置

#添加主题
class BaseSetting(object):
    enable_themes = True  #开启主题功能
    use_bootswatch = True #是否可以切换主题

class GlobleSetting(object):
    site_title = "自动化测试平台"
    site_footer ="微哨测试组"
    menu_style = "accordian"


xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobleSetting)


