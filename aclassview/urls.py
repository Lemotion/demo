from django.conf.urls import url

from aclassview import views

urlpatterns = [
    #视图函数的路由
    # url(r'^aclassview/$',views.index),
    #类视图的路由
    url(r'^aclassview/$',views.LoginView.as_view())
]