# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from bridge.models import build_obligation_map
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from authorization.models import User

build_obligation_map()


class UserDetailView(LoginRequiredMixin, DetailView):
    """
    Shows a :class:`User` information
    """
    model = User


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'authorization/user_detail.html'
