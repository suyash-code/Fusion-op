from django.conf.urls import url

from . import views

app_name = 'ps1'

urlpatterns = [

    url(r'^$', views.ps1, name='ps1'),
    url(r'^inwardIndent/$', views.inward, name='inward'),
    url(r'^indentview2/(?P<id>\d+)$', views.indentview2, name='indentview2'),
    url(r'^forwardindent/(?P<id>\d+)/$', views.forwardindent, name='forwardindent'),
]
