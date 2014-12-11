from django.conf.urls import patterns, url, include
from .views import index, login, monitor, exceptionip, logout, handlelog
urlpatterns = patterns('',
    url(r'^$', login, name="home"),
    url(r'^/monitor$', monitor, name="monitorlog"),
    url(r'^/exception$', exceptionip, name="exceptionip"),
    url(r'^/logout$', logout, name="logout"),
    url(r'^/handled$', handlelog),
)
