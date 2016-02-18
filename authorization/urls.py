# -*- coding: utf-8 -*-
from django.conf.urls import url
from authorization import views

urlpatterns = [
    url(
            r'^(?P<pk>\d+)$',
            views.UserDetailView.as_view(),
            name='user'
    ),
]
