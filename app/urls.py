# coding: utf-8

from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^composer/', include('composer.urls')),

    url(r'', TemplateView.as_view(template_name="index.html")),
]
