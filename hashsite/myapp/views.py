from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from hashsite.myapp.forms import DocumentForm
import hashlib

import binascii
from btctxstore import BtcTxStore


def do_transaction(sha256hash):
    wifs = ["cT99WqxmPghVpeqwmxtXbMQwPK1BFpKcejWS5L84KGR14va2hQ4W"]

    # use testnet and dont post tx to blockchain for example
    api = BtcTxStore(testnet=True)

    # store data in blockchain as nulldata output (max 40bytes)
    data = sha256hash.encode(encoding='utf-8')
    txid = api.store_nulldata(data, wifs)

    return txid



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

            # dochash = form.cleaned_data['dochash']
            #
            # if dochash:
            #     if dochash.upper() == sha256sum.upper():
            #         return HttpResponse('<p style="color:green">Hash is correct!</p>')
            #     else:
            #         return HttpResponse('<p style="color:red">Hash is NOT correct!</p>')
            # else:
            #     return HttpResponse("SHA256: "+sha256sum)

            done_tx = do_transaction(sha256sum)
            return HttpResponse('SHA256: '+sha256sum+'<br><br><a href="https://www.blocktrail.com/tBTC/tx/'+done_tx+'">'+'TX on Blocktrail.com</a>')

        else:
            return HttpResponse("Form is not valid!")
    else:
        return HttpResponse("GET-request?! Are you serious?")
