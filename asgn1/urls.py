from django.conf.urls import patterns, include, url
from django.contrib import admin
from journal import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'asgn1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    
    url(r'^journal/$', views.entry_list, name='entry_list'),
    url(r'^entry/(?P<entry_id>\d+)$', views.entry, name='detail'),
    url(r'^admin/', include(admin.site.urls)),
)
