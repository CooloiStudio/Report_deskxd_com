from django.conf.urls import include, url
from turanga import views

urlpatterns = [

    url(r'^$', views.IndexViews.as_view(), name='index'),

    url(r'^crash/$', views.crash, name='crash'),

]
