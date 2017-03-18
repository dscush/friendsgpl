from django.conf.urls import include, url
from django.contrib import admin
from adminplus.sites import AdminSitePlus
import friends.views

admin.site = AdminSitePlus()
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'friends.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', friends.views.home, name='home'),
    url(r'^about/$', friends.views.about, name='about'),
    url(r'^contact/$', friends.views.contact, name='contact'),
    url(r'^join/$', friends.views.join, name='join'),
    url(r'^downunder/$', friends.views.downunder, name='downunder'),
    url(r'^admin/', include(admin.site.urls)),
]
