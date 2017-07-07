from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<pk>[0-9]+)$', views.TabletDetailView.as_view(), name='tablet_detail'),
    url(r'^create/$', views.TabletCreate.as_view(), name='tablet_create'),
    url(r'^update/(?P<pk>[0-9]+)$', views.TabletUpdate.as_view(), name='tablet_update'),
    url(r'^delete/(?P<pk>[0-9]+)$', views.TabletDelete.as_view(), name='tablet_delete'),
    url(r'^seals/(?P<pk>[0-9]+)$', views.SealDetailView.as_view(), name='seal_detail'),
    url(r'^seals/create/$', views.SealCreate.as_view(), name='seal_create'),
    url(r'^seals/update/(?P<pk>[0-9]+)$', views.SealUpdate.as_view(), name='seal_update'),
    url(r'^seals/delete/(?P<pk>[0-9]+)$', views.SealDelete.as_view(), name='seal_delete'),
]
