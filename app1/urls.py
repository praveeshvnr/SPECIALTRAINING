import imp
from django.urls import URLPattern,re_path,include
from .import views


urlpatterns=[
    re_path(r'^$', views.branchreg, name="branchreg"),
    re_path(r'^branchsignup$', views.branchsignup, name="branchsignup"),
    re_path(r'^branchlog$', views.branchlog, name="branchlog"),
    re_path(r'^branchlogin$', views.branchlogin, name="branchlogin"),

    re_path(r'^empreg$', views.empreg, name="empreg"),



]