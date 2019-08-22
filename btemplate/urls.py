from django.urls import path

from btemplate import views

urlpatterns =[
    path('btemplate/',views.index)
]