# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Asdf
from django_pmedien_defaults.pmedien_defaults import PmedienDefaults

admin.site.register(Asdf, PmedienDefaults)
