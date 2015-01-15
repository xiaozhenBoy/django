# -*- coding: utf-8 -*-
# 消息处理设备的管理
# 实现了消息设备的查看，增加，修改和删除功能

# 注：目前只是将主要设计了功能的框架，实现逻辑暂无

from django.shortcuts import render_to_response
from django.template.context import RequestContext

from DeviceMana.forms.messdev_forms import MessdevForm

def messdevMana(request):
    return render_to_response('message_dev.html', RequestContext(request, {}))

def messdevAdd(request):
    form = MessdevForm()
    return render_to_response('message_dev_add.html', RequestContext(request, {'form':form}))

def messdevAlter(request):
    form = MessdevForm(initial={'date':'20150112', 
                              'subject':'modification test', 'message':'This the modification'}) # test
    return render_to_response('message_dev_add.html', RequestContext(request, {'form':form}))

def messdevDel(request):
    return render_to_response('message_dev_del.html', RequestContext(request, {}))
