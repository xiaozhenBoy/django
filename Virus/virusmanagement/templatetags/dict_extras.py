#coding:utf-8
from django import template

register = template.Library()

@register.filter(name='getDictValue')
def getDictValue(var, key):
    # var is a dict, according the key, return the value.
    return var[key]
