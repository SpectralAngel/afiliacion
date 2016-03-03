# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from bridge.models import Affiliate
from django.core.management.base import BaseCommand
from django.db.models.aggregates import Max
from django.utils.translation import ugettext_lazy as _
import re

from authorization.models import User


class Command(BaseCommand):
    help = "Creates the missing users based in the :class:`Affiliate` data"

    def handle(self, *args, **options):
        non_decimal = re.compile(r'[^\d.]+')

        max_created = User.objects.aggregate(
                max=Max('affiliate_id')
        )['max']
        if max_created is None:
            max_created = 0

        affiliates = Affiliate.objects.filter(
                id__gt=max_created,
                card_id__isnull=False,
        )

        print(_("Creando {0} usuarios").format(affiliates.count()))
        print(_('Iniciando con el {0}').format(max_created + 1))

        [User.objects.create_user(
                '{0}'.format(a.id),
                a.email,
                re.sub("[^0-9]", "", a.card_id),
                first_name=a.first_name,
                last_name=a.last_name,
                affiliate=a,
        ) for a in affiliates]
