from django.shortcuts import render, render_to_response
from django.template.context import RequestContext

# Create your views here.
def index(request):
    return render_to_response('index.html', RequestContext(request, {}))

