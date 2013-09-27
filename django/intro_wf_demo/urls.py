from django.conf.urls import patterns, include, url
from splunkdj.utility.views import render_template as render

urlpatterns = patterns('',
    url(r'^home/$', render('intro_wf_demo:home.html'), name='home'),
    url(r'^custom_viz/$', render('intro_wf_demo:custom_viz.html'), name='custom_viz'),
    url(r'^drilldown/$', render('intro_wf_demo:drilldown.html'), name='drilldown'),
)
