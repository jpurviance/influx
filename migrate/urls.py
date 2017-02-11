from django.conf.urls import url

from . import views

app_name = "migrate"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^resources/$', views.resources, name='resources')
]
