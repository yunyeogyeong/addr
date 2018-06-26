from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.addr_list, name='addr_list'),
]