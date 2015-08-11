#!usr/bin/env python
# coding: utf-8

from django.conf.urls import url
from panel.views import Home

urlpatterns = [
    url(r'^$', Home.as_view()),
]
