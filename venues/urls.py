from django.conf.urls import url

from . import views


app_name = 'venues'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<venue_id>[0-9]+)/$', views.detail, name='detail'),
]