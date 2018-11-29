from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from . import views
from website.models import Page

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^join/$', views.join, name='join'),
    url(r'^volunteer/$', views.volunteer, name='volunteer'),
    url(r'^downunder/$', views.downunder, name='downunder'),

    url(r'^summernote/', include('django_summernote.urls')),

    url(r'^payment/(completed|canceled)/$', views.payment_return, name='payment_return'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

for page in Page.objects.all():
    # TODO: Refactor this. This design pattern is bad. This needs to be
    # commented out in order for the migration creating the Page model runs, and
    # the entire app needs to be restarted in order for new page records to
    # become available here, since this code runs only on startup.
    urlpatterns.append(url(r'^{}/$'.format(page.slug), views.page))
