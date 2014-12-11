#coding:utf-8
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect

from .forms import LoginForm

from datetime import datetime, timedelta, date

from virusmanagement.models import Superfw, Syslogd, Viruslog, Handlelog

# Create your views here.
def index(request):
    return render_to_response('index.html', RequestContext(request,{}))
def login(request):
    if request.method == 'GET':
        if request.user is not None and request.user.is_active:
            return index(request)
        form = LoginForm()
        return render_to_response('login.html', RequestContext(request,{'form':form}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return render_to_response('index.html', RequestContext(request))
            else:
                return render_to_response('login.html', RequestContext(request,{'form':form,'password_is_wrong':True}))
        else:
            return render_to_response('login.html', RequestContext(request,{'form':form}))
@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/virusmanagement')
def monitor(request):
    user = request.user # check user state, if active, display information
    if user is not None and user.is_active:
        # current there three types of the log
        mlogs = []
        # set the conditiona of queries, latest 3 days
        now = datetime.now()
        threedays = timedelta(days=3)
        time_limit = now - threedays
        # begin to query
        v_logs = Viruslog.objects.values('severity', 'time', 'device_id', 'get_virus_device_ip','spread_virus_device_ip', 'virus_name', 'threat_type', 'danger_type').filter(time__gt=time_limit)
        for item in v_logs:
            item["logtype"]='viruslog'
        mlogs.extend(v_logs)
        fw_logs = Superfw.objects.values('severity', 'time', 'device_id', 'login_ip', ).filter(time__gt=time_limit)
        for item in fw_logs:
            item["logtype"]='loginlog'
        mlogs.extend(fw_logs)
        # sort mlogs according log_time
        mlogs.sort(key=lambda x:x['time'], reverse=True)
        # construct paginator objector for multi_page
        paginator = Paginator(mlogs, 10)
        page = request.GET.get('page')
        try:
            show_logs = paginator.page(page)
        except PageNotAnInteger:
            show_logs = paginator.page(1)
        except EmptyPage:
            show_logs = paginator.page(paginator.num_pages)
        return render_to_response('monitor_log.html', RequestContext(request, {'mlogs':show_logs,}))
    else:
        return login(request)
def exceptionip(request):
    user = request.user # check user state, if active, display information
    if user is not None and user.is_active:
        if request.method == 'GET':
            # set the condition of queries, latest 3 days
            now = datetime.now()
            threedays = timedelta(days=3)
            time_limit = now - threedays
            exp_ips = Viruslog.objects.values('indx','severity', 'time', 'virus_name', 'get_virus_device_ip','spread_virus_device_ip').filter(time__gt=time_limit)
            paginator = Paginator(exp_ips, 10)
            page = request.GET.get('page')
            try:
                show_ips = paginator.page(page)
            except PageNotAnInteger:
                show_ips = paginator.page(1)
            except EmptyPage:
                show_ips = paginator.page(paginator.num_pages)
            return render_to_response('exception.html', RequestContext(request, {'ips':show_ips,}))
        if request.method == 'POST':
            # get checkbox value (viruslog indx)
            check_box_list = request.REQUEST.getlist('box_child')
            vlog_indx_list = [ int(item) for item in check_box_list]
            # handle abnormal ip according the selected operation
            if 'ip_reject' in request.POST:
                ip_reject_list = []
                for indx in vlog_indx_list:
                    vlog = Viruslog.objects.get(indx=indx)
                    vlog.is_handled = True
                    ip_reject_list.append(vlog.get_virus_device_ip)
                    ip_reject_list.append(vlog.spread_virus_device_ip)
                    vlog.save()
                    # create handle log
                    hlog = Handlelog(device_name=vlog.get_virus_device_name,device_ip=vlog.get_virus_device_ip,is_victim='VICTIM',operation='REG',op_time=date.today())
                    hlog.save()
                    hlog = Handlelog(device_name=vlog.spread_virus_device_name,device_ip=vlog.spread_virus_device_ip,is_victim='VSOURCE',operation='REG',op_time=date.today())
                    hlog.save()
                # write and execu control script
                # redirect to handle log page
                return HttpResponseRedirect('/virusmanagement/handled')
            else:
                return HttpResponseRedirect('/virusmanagement/exception')
        else:
            return login(request)
    else:
        return login(request)
def handlelog(request):
    user = request.user
    if user is not None and user.is_active:
        if request.method == 'GET':
            hlogs = Handlelog.objects.all()
            print hlogs
            paginator = Paginator(hlogs, 10)
            page = request.GET.get('page')
            try:
                show_logs = paginator.page(page)
            except PageNotAnInteger:
                show_logs = paginator.page(1)
            except EmptyPage:
                show_logs = paginator.page(paginator.num_pages)
            return render_to_response('handle_log.html', RequestContext(request, {'hlogs':show_logs,}))
        if request.method == 'POST':
            # get checkbox value (viruslog indx)
            check_box_list = request.REQUEST.getlist('box_child')
            hlog_id_list = [ int(item) for item in check_box_list]
            # handle abnormal ip according the selected operation
            # in general, some abnormal ip need to recovery to normal
            if 'ip_recovery' in request.POST:
                # write control script
                # modify ip state in handlelog table
                for hlog_id in hlog_id_list:
                    hlog = Handlelog.objects.get(id=hlog_id)
                    hlog.operation = 'OTH'
                    hlog.op_time=date.today()
                    hlog.save()
            return HttpResponseRedirect('/virusmanagement/handled')
    else:
        return login(request)
