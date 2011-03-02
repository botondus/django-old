from django.conf.urls.defaults import *
from regressiontests.templates import views
from regressiontests.templates.admin import basic_site, advanced_site 

urlpatterns = patterns('',
    #We need 2 admin site instances to test inclusion tag behaviour. Refs #15070
    (r'^basic-admin/', include(basic_site.urls, app_name='basic')),
    (r'^advanced-admin/', include(advanced_site.urls, app_name='advanced')),
    (r'^inclusion-tag-view/$', views.use_inclusion_tag),
)