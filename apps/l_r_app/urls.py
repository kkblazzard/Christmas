from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.home_page),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^process$', views.process),
    url(r'^dashboard', views.dashboard),
    url(r'^logout$', views.logout),
    url(r'^(?P<id>\d+)/edit$', views.edit),
    url(r'^update/(?P<id>\d+)$', views.update),
    url(r'^(?P<id>\d+)/delete$', views.delete_user_from_db),
]