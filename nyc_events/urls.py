from django.conf.urls import patterns, include, url
from app import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^analyze/(\d+)$', views.analyze, name='analyze'),
    url(r'^home$', views.home, name='home'),
    url(r'^home/(?P<dbn>\w+)$', views.home, name='home'),
    url(r'^home/(?P<dbn>\w+)/(?P<teacher_id>\d+)$', views.home, name='home'),
    url(r'^load', views.load, name='load'),
    url(r'^admin/', include(admin.site.urls)),
)
