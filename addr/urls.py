from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.addr_list, name='addr_list'),
    url(r'^addr/(?P<pk>\d+)/$', views.addr_detail, name='addr_detail'),
]