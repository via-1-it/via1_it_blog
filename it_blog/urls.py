from django.conf.urls import url
from . import views

urlpatterns = [
  path('^$', views.index, name='index')
  path('^About/', views.index, name = "About"),
  path('^Posts/', views.index, name = 'Posts'),
];



