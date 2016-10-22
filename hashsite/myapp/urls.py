# -*- coding: utf-8 -*-
from django.conf.urls import url
from hashsite.myapp.views import form_view, sha1hash_view
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^form/$', form_view, name='form_view_name'),
    url(r'^sha1hash/$', sha1hash_view, name='sha1hash_view_name'),
    url(r'^$', RedirectView.as_view(url='form/', permanent=True))

]
