from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#定义类视图
from django.views import View


class LoginView(View):
    def get(self,request):
        # 处理GET请求，返回注册页面
        return HttpResponse('视图函数-----GET------登录页面')

    def post(self,reqeust):
        # 处理POST请求，实现注册逻辑
        return HttpResponse('视图函数-----POST------登录请求')

def index(request):
    # 获取请求方法，判断是GET/POST请求
    if request.method == 'GET':
        # 处理GET请求，返回注册页面
        return HttpResponse('视图函数-----GET------登录页面')
    else:
        # 处理POST请求，实现注册逻辑
        return HttpResponse('视图函数-----POST------登录请求')