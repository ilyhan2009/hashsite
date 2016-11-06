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


def sha256hash_view(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            sha256 = hashlib.sha256()
            for chunk in request.FILES['docfile'].chunks():
                sha256.update(chunk)
            sha256sum = sha256.hexdigest()
            dochash = form.cleaned_data['dochash']

            if dochash:
                if dochash.upper() == sha256sum.upper():
                    return HttpResponse('<p style="color:green">Hash is correct!</p>')
                else:
                    return HttpResponse('<p style="color:red">Hash is NOT correct!</p>')
            else:
                return HttpResponse("SHA256: "+sha256sum)
        else:
            return HttpResponse("Form is not valid!")
    else:
        return HttpResponse("GET-request?! Are you serious?")
