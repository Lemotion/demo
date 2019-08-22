from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    #渲染模板
    return render(request,'index.html')