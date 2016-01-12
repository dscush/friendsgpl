from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'friends.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'friends.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
]
