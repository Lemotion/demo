#过滤器函数
from django import template

register = template.Library()

@register.filter
def multi(x):
    return x*x