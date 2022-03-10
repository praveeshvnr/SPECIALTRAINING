from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import re_path, include
from .import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^firstpage$', views.firstpage, name='firstpage'),
    re_path(r'', include('app.urls')),

    re_path(r'^second/$', views.second, name='second'),
    re_path(r'app1/', include('app1.urls')),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)