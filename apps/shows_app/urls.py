from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^all_shows$', views.all_shows),
    url(r'^(?P<network>\w+)/network$', views.network),
    url(r'^city$', views.city),
    url(r'^country$', views.country),
    url(r'^SyFy_horror$', views.syfy),
    url(r'^add/(?P<id>\d+)$', views.add),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^rate/(?P<id>\d+)$', views.rate),
]