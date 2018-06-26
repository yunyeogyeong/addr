from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.addr_list, name='addr_list'),
    url(r'^addr/(?P<pk>\d+)/$', views.addr_detail, name='addr_detail'),
    url(r'^addr/new/$', views.addr_new, name='addr_new'),
    url(r'^addr/(?P<pk>\d+)/edit/$', views.addr_edit, name='addr_edit'),
    url(r'^drafts/$', views.addr_draft_list, name='addr_draft_list'),
    url(r'^addr/(?P<pk>\d+)/publish/$', views.addr_publish, name='addr_publish'),
    url(r'^addr/(?P<pk>\d+)/remove/$', views.addr_remove, name='addr_remove'),
]