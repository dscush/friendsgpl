from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^join/$', views.join, name='join'),
    url(r'^downunder/$', views.downunder, name='downunder'),
]
