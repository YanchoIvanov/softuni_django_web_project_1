from django.http import HttpResponseRedirect
from django.shortcuts import render

from vegastroy.ask_for_offer.forms import AskForOfferForm


def ask_for_offer(request):
    if request.method == 'POST':
        form = AskForOfferForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/ask_for_offer/success/")

    form = AskForOfferForm
    context = {
        'form': form
    }
    return render(request, 'ask_for_offer/contact_form.html', context)


def success(request):
    return render(request, 'ask_for_offer/success.html')
