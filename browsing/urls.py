from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'tablets/$', views.TabletListView.as_view(), name='browse_tablets'),
    url(r'seals/$', views.SealListView.as_view(), name='browse_seals'),
]
