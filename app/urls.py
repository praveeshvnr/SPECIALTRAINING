from xml.dom.minidom import Document
from django.urls import URLPattern, re_path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    re_path(r'^$', views.index, name="index"),
    re_path(r'^loginpage$', views.loginpage, name="loginpage"),
    re_path(r'^signup$', views.signup, name="signup"),
    re_path(r'^login$', views.login, name="login"),
    re_path(r'^companyregistration$', views.companyregistration, name="companyregistration"),
    re_path(r'^companysignup$', views.companysignup, name="companysignup"),
    re_path(r'^companypage$', views.companypage, name="companypage"),
    re_path(r'^logout$', views.logout, name="logout"),
    

    


    # re_path(r'^devissues/(?P<id>\d+)$', views.devissues, name='devissues'),

    
]
