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
        }
    }

    #渲染模板
    return render(request,'index.html',context=content)