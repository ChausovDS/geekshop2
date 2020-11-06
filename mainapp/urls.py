from django.urls import re_path

import mainapp.views as mainapp

from .apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    re_path(r"^$", mainapp.products, name="index"),
    re_path(r"^category/(?P<pk>\d+)/$", mainapp.products, name="category"),
    re_path(r"^product/(?P<pk>\d+)/$", mainapp.product, name="product"),
    re_path(r"^category/(?P<pk>\d+)/page/(?P<page>\d+)/$", mainapp.products, name="page"),
]
