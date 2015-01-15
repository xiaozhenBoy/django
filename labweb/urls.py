from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import index

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index, name='index'),
)
