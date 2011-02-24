# coding: utf-8
from django.conf.urls.defaults import *
from regressiontests.templates import views
from regressiontests.templates.admin import basic_site, advanced_site 

urlpatterns = patterns('',

    # Test urls for testing reverse lookups
    (r'^$', views.index),
    (r'^client/([\d,]+)/$', views.client),
    (r'^client/(?P<id>\d+)/(?P<action>[^/]+)/$', views.client_action),
    (r'^client/(?P<client_id>\d+)/(?P<action>[^/]+)/$', views.client_action),
    url(r'^named-client/(\d+)/$', views.client2, name="named.client"),

    # Unicode strings are permitted everywhere.
    url(ur'^Юникод/(\w+)/$', views.client2, name=u"метка_оператора"),
    url(ur'^Юникод/(?P<tag>\S+)/$', 'regressiontests.templates.views.client2', name=u"метка_оператора_2"),
    
    #
    (r'^basic-admin/', include(basic_site.urls, app_name='basic')),
    (r'^advanced-admin/', include(advanced_site.urls, app_name='advanced')),
    (r'^inclusion-tag-view/$', views.use_inclusion_tag),
)
