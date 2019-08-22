from django.conf.urls import url

from aclassview import views

urlpatterns = [
    #视图函数的路由
    # url(r'^aclassview/$',views.index),
    #类视图的路由
    #给类添加装饰器
    #url(r'^aclassview/$',views.LoginView.as_view())
    #使用装饰器功能的扩展类
    url(r'^aclassview/$',views.LoginView_Decorator_Mixin.as_view())
]