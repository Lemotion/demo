from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator

from django.views import View
# Create your views here.

#1. 写一个扩展类（新功能 给所有的类添加 装饰器）
class DecoratorMixin(object):
    @classmethod
    def as_view(cls,*args,**kwargs):
        # 1.通过多继承的父类 实现 返回视图函数
        view = super().as_view(*args,**kwargs)
        # 2.给视图函数添加装饰器
        view = my_decorator(view)
        return view

def my_decorator(func):
    def wrapper(request,*args,**kwargs):
        print('添加了装饰器----函数')
        print(request.method,request.path)
        return func(request,*args,**kwargs)
    return wrapper

@method_decorator(my_decorator,name='dispatch')
#定义类视图 添加装饰器
class LoginView_Decorator_Mixin(DecoratorMixin,View):
    # @method_decorator(my_decorator)
    def get(self,request):
        # 处理GET请求，返回注册页面
        return HttpResponse('视图函数-----Mixin装饰器-----GET------登录页面')

    # @method_decorator(my_decorator)
    def post(self,reqeust):
        # 处理POST请求，实现注册逻辑
        return HttpResponse('视图函数-----Mixin装饰器-----POST------登录请求')

# class LoginView_Decorator(View):
#     # @method_decorator(my_decorator)
#     def get(self,request):
#         # 处理GET请求，返回注册页面
#         return HttpResponse('视图函数-----装饰器-----GET------登录页面')
#
#     # @method_decorator(my_decorator)
#     def post(self,reqeust):
#         # 处理POST请求，实现注册逻辑
#         return HttpResponse('视图函数-----装饰器-----POST------登录请求')


# def index(request):
#     # 获取请求方法，判断是GET/POST请求
#     if request.method == 'GET':
#         # 处理GET请求，返回注册页面
#         return HttpResponse('视图函数-----GET------登录页面')
#     else:
#         # 处理POST请求，实现注册逻辑
#         return HttpResponse('视图函数-----POST------登录请求')