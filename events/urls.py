from django.conf.urls import url, include
from . import views



urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^all/', views.all, name='all'),
    url(r'^go/(?P<pk>[0-9]+)/$', views.go, name='go'),
]