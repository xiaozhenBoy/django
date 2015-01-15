from django.shortcuts import render, render_to_response
from django.template.context import RequestContext

# Create your views here.
def policyMana(request):
    return render_to_response('policy.html', RequestContext(request, {}))

