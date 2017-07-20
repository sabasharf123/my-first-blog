from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
