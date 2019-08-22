from datetime import date

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):

    content = {
        "name":"老王",
        "age":88,
        "son":[
            "小明",
            "小王",
            "大头儿子",
        ],
        "wife":{
            "name":"小丽"
        },
        "date_time":date(2008,1,1),
        "data":"<a>百度链接</a>"
    }

    #渲染模板
    return render(request,'jinja2index.html',context=content)