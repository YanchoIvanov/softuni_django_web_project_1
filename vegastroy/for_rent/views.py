from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Item
from .forms import AvailabilityRequestForm


def item_list(request):
    items = Item.objects.all()

    context = {
        'items': items,
    }

    return render(request, 'for_rent/item_list.html', context)


@login_required
def item_details(request, pk):
    item = get_object_or_404(Item, pk=pk)
    form = AvailabilityRequestForm()
    if request.method == 'POST':
        form = AvailabilityRequestForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            item.availability = False
            item.save()
            return HttpResponseRedirect('success/')

    context = {
        'item': item,
        'form': form,
    }

    return render(request, 'for_rent/item_details.html', context)


def success_for_rent(request, pk):
    pk = Item.pk
    return render(request, 'for_rent/success_for_rent.html')
