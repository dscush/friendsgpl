from django.conf.urls import include, url
from django.contrib import admin
from adminplus.sites import AdminSitePlus

admin.site = AdminSitePlus()
admin.autodiscover()

urlpatterns = [
    url(r'^', include('website.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
