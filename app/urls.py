# coding: utf-8

from django.conf.urls import url, include, handler400, handler403, handler404, handler500
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render_to_response
from django.views.generic import TemplateView

import app.views

from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^composer/', include('composer.urls')),

    url(r'^loader/', app.views.loader),

    url(r'^cv/$', TemplateView.as_view(template_name="cv.html")),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler400 = handler403 = handler404 = handler500 = 'app.urls.error_index'


def error_index(request):
    return render_to_response('index.html')
