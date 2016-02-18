# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.urlresolvers import reverse
from django.db import models
from bridge import models as bmodels


class AUserManager(UserManager):
    def get_queryset(self):
        return super(AUserManager, self).get_queryset().select_related(
                'affiliate',
        ).prefetch_related(
                'affiliate__cuotatable_set',
                'affiliate__loan_set',
                'affiliate__loan_set__pay_set'
        )


class User(AbstractUser):
    affiliate = models.ForeignKey(bmodels.Affiliate, null=True, blank=True)

    objects = AUserManager()

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Returns the short name for the user."""
        return self.first_name

    def get_absolute_url(self):
        """
        Obtains the absolute url for each :class:`User`
        """
        return reverse('user', args=[self.id])
