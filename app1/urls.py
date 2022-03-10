import imp
from django.urls import URLPattern,re_path,include
from .import views


urlpatterns=[
    re_path(r'^$', views.branchreg, name="branchreg"),
    re_path(r'^branchsignup$', views.branchsignup, name="branchsignup"),
    re_path(r'^branchlog$', views.branchlog, name="branchlog"),
    re_path(r'^branchlogin$', views.branchlogin, name="branchlogin"),
    re_path(r'^employeereg$', views.employeereg, name="employeereg"),
    re_path(r'^employeeshow$', views.employeeshow, name="employeeshow"),
    re_path(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    re_path(r'^empedit/(?P<id>\d+)$', views.empedit, name='empedit'),
    re_path(r'^update/(?P<id>\d+)$', views.update, name='update'),


    re_path(r'^empreg$', views.empreg, name="empreg"),



]