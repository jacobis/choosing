from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

from polls import views as polls_views
from accounts import views as accounts_views

urlpatterns = [
    url(r'^$', polls_views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login),
    url(r'^logout/$', accounts_views.logout),
    url(r'^accounts/', include('authtools.urls')),
    url(r'^groups/$', accounts_views.index_group, name='index_group'),
    url(r'^groups/create/$', accounts_views.create_group, name='create_group'),
    url(r'^groups/(?P<group_id>[0-9]+)/$', accounts_views.detail_group, name='detail_group'),
    url(r'^polls/', include('polls.urls')),
    url(r'^venues/', include('venues.urls')),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
