from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pro_id>", views.pro, name="pro"),
    # re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail)
]
