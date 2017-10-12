from django.conf.urls import patterns, include, url
from django.contrib import admin
from app01 import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_08bbs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', views.login),
    url(r'^index/', views.index),
    url(r'^addfavor/', views.addfavor),
    url(r'^getreply/', views.getreply),
    url(r'^submitreply/', views.submitreply),
    url(r'^submitchat/', views.submitchat),
    url(r'^getchart/', views.getchart),
    url(r'^getchart2/', views.getchart2),
    url(r'^api/', include('app01.urls')),
)
