from django.conf.urls import patterns, include, url
from splunkdj.utility.views import render_template as render

urlpatterns = patterns('',
    url(r'^home/$', 'intro_wf_demo.views.home', name='home'), 
)
