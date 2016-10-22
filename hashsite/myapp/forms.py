# -*- coding: utf-8 -*-

from django import forms


class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select a file')
    dochash = forms.CharField(label='Your SHA1 hash', max_length=100)
