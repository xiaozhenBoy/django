from django.conf.urls import patterns, include, url
from .views import index, probeMana, probeAdd, probeAlter, probeDel
from .views import ipMana
from .views import messdevMana, messdevAdd, messdevAlter, messdevDel
from .views import policyMana

urlpatterns = patterns('',
		url(r'index/$', index, name='index'),
        url(r'probemana/$', probeMana, name='probe'),
        url(r'probeadd/$', probeAdd, name='probeadd'),
        url(r'probealter/', probeAlter, name='probealter'),
        url(r'probedel/', probeDel, name='probedel'),
        url(r'ipmana/$', ipMana, name='ip'),
        url(r'messdevmana/$', messdevMana, name='messdev'),
        url(r'messdevadd/$', messdevAdd, name='messdevadd'),
        url(r'messdevalter/', messdevAlter, name='messdevalter'),
        url(r'messdevdel/', messdevDel, name='messdevdel'),
        url(r'policymana/$', policyMana, name='poicy'),
)
