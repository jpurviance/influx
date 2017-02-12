from django.conf.urls import url

from . import views, api

app_name = "migrate"
urlpatterns = [
    url(r'^api/$', api.add, name='add'),
    url(r'api/visa/$', api.visa, name='visa'),
    url(r'api/reverse_visa/$', api.reverse_visa, name='reverse_visa'),
    url(r'^$', views.index, name='index'),
    url(r'^resources/$', views.resources, name='resources'),
    url(r'^visaview/$', views.visaview, name='visaview')
]
