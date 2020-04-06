from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^api/execGoogleApiTask$', views.asyncGoogleDirectionTask, name='direction'),
    url(r'^api/getResult/(?P<task_id>[^/]+)/$', views.getResult, name='result')
]
