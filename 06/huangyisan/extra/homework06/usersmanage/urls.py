from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home', views.home, name='home'),
    url(r'^usersinfo', views.usersinfo, name='usersinfo'),
    url(r'^create', views.create, name='create'),
    url(r'^delete', views.delete, name='delete'),
    url(r'^save/', views.save, name='save'),
]
