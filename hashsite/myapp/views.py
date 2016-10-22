from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from hashsite.myapp.forms import DocumentForm
import hashlib


def form_view(request):
    form = DocumentForm()  # A empty, unbound form

    # Render list page with the documents and the form
    return render(request, 'form.html', {'form': form})


def sha1hash_view(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            sha1 = hashlib.sha1()
            for chunk in request.FILES['docfile'].chunks():
                sha1.update(chunk)
            sha1sum = sha1.hexdigest()
            dochash = form.cleaned_data['dochash']

            if dochash:
                if dochash.upper() == sha1sum.upper():
                    return HttpResponse('<p style="color:green">Hash is correct!</p>')
                else:
                    return HttpResponse('<p style="color:red">Hash is NOT correct!</p>')
            else:
                return HttpResponse("SHA1: "+sha1sum)
        else:
            return HttpResponse("Form is not valid!")
    else:
        return HttpResponse("GET-request?! Are you serious?")
