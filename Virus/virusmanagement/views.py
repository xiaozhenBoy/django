from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect

from .forms import LoginForm

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
    #user = request['user']
    if True:#user is not None and user.is_active:
        lines = []
        for i in xrange(10000):
            lines.append(u"Line %s" % (i+1))
        paginator = Paginator(lines, 10)
        page = request.GET.get('page')
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            show_lines = paginator.page(1)
        except EmptyPage:
            show_lines = paginator.page(paginator.num_pages)
        return render_to_response('monitor_log.html', RequestContext(request, {'lines':show_lines,}))
        #return render_to_response('monitor_log.html', RequestContext(request))
    else:
        return login(request)
def exceptionip(request):
    ips = []
    for i in xrange(100):
        ips.append(u'192.168.140.%s' % i)
    paginator = Paginator(ips, 10)
    page = request.GET.get('page')
    try:
        show_ips = paginator.page(page)
    except PageNotAnInteger:
        show_ips = paginator.page(1)
    except EmptyPage:
        show_ips = paginator.page(paginator.num_pages)
    return render_to_response('exception.html', RequestContext(request, {'ips':show_ips,}))
