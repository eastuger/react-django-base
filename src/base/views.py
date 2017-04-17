# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

class IndexView(View):
    """Render main page"""
    def get(self, request):
        """Return HTML for main app"""

        abspath = open(os.path.join(settings.BASE_DIR, 'static/src/index.html'), 'r')
        return HttpResponse(content=abspath.read())
