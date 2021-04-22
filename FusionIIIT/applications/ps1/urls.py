from django.conf.urls import url

from . import views

app_name = 'ps1'

urlpatterns = [

    url(r'^$', views.ps1, name='ps1'),
    url(r'^composed_indents/$', views.composed_indents, name='composed_indents'),
    url(r'^indentview/(?P<id>\d+)$', views.indentview, name='indentview'),
    url(r'^inwardIndent/$', views.inward, name='inward'),
    url(r'^indentview2/(?P<id>\d+)$', views.indentview2, name='indentview2'),
    url(r'^confirmdelete/(?P<id>\d+)$', views.confirmdelete, name='confirm_delete'),
    url(r'^delete/(?P<id>\d+)$',views.delete, name='delete'),
    url(r'^forwardindent/(?P<id>\d+)/$', views.forwardindent, name='forwardindent'),
]
