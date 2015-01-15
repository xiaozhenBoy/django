# -*- coding: utf-8 -*-
# 异常IP的管理
# 实现了异常IP的查看，控制

from django.shortcuts import render_to_response
from django.template.context import RequestContext

from DeviceMana.forms.ip_forms import SkimConForm

def ipMana(request):
    form = SkimConForm()
    ip = {'indx':18}
    return render_to_response('ip.html', RequestContext(request, {'form':form, 'ip':ip}))
