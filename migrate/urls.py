from django.conf.urls import url

from . import views, api

app_name = "migrate"
urlpatterns = [
    url(r'^api/$', api.add, name='add'), 
    url(r'^$', views.index, name='index'),
    url(r'^resources/$', views.resources, name='resources')
]
