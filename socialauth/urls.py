"""
INTEGRATE EVENTBRITE OAUTH LOGIN IN OUR DJANGO PROJECT
by Cristian Moyano

"""
from django.conf.urls import url, include
from django.contrib import admin
from events.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^events/', include('events.urls', namespace='events')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
]
