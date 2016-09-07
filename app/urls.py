# coding: utf-8

from django.conf.urls import url, include, handler400, handler403, handler404, handler500
from django.contrib import admin
from django.shortcuts import render_to_response
from django.views.generic import TemplateView

import app.views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^composer/', include('composer.urls')),
    
    url(r'^loader/', app.views.loader),

    url(r'^loader/', apps.views.loader),
    url(r'', TemplateView.as_view(template_name="index.html")),
]


handler400 = handler403 = handler404 = handler500 = 'app.urls.error_index'


def error_index(request):
    return render_to_response('index.html')
