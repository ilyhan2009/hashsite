# -*- coding: utf-8 -*-
from django.conf.urls import url
from hashsite.myapp.views import form_view, sha256hash_view
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^form/$', form_view, name='form_view_name'),
    url(r'^sha256hash/$', sha256hash_view, name='sha256hash_view_name'),
    url(r'^$', RedirectView.as_view(url='form/', permanent=True))

]
