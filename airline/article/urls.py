from django.contrib import admin
from django.urls import include, path, re_path
from django.http import HttpResponse
# from django.conf.urls import url
from .import views

urlpatterns = [
    # url(r'^$', views.article_list),
    re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail)
]
