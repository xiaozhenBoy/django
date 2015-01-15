# -*- coding: utf-8 -*-
# 探针设备的管理
# 实现了探针的查看，增加，修改和删除功能

from django.shortcuts import render_to_response
from django.template.context import RequestContext

from DeviceMana.forms.probe_forms import ProbeForm

def probeMana(request):
    return render_to_response('probe.html', RequestContext(request, {}))

def probeAdd(request):
    form = ProbeForm()
    return render_to_response('probe_add.html', RequestContext(request, {'form':form}))

def probeAlter(request):
    form = ProbeForm(initial={'date':'20150112', 
                              'subject':'modification test', 'message':'This the modification'}) # test
    return render_to_response('probe_add.html', RequestContext(request, {'form':form}))

def probeDel(request):
    return render_to_response('probe_del.html', RequestContext(request, {}))
