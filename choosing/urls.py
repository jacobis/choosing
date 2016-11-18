from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

from polls import views as polls_views

urlpatterns = [
    url(r'^$', polls_views.home, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^accounts/', include('authtools.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^venues/', include('venues.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # import debug_toolbar
    # urlpatterns += [
    #     url(r'^__debug__/', include(debug_toolbar.urls)),
    # ]
