from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import AvailabilityRequestForm


def item_list(request):
    items = Item.objects.all()
    return render(request, 'for_rent/item_list.html', {'items': items})


@login_required
def item_details(request, pk):
    item = get_object_or_404(Item, pk=pk)
    form = AvailabilityRequestForm()
    if request.method == 'POST':
        form = AvailabilityRequestForm(request.POST)
        if form.is_valid():
            # Here you can handle the availability request, e.g., send an email to the admin
            pass
    return render(request, 'for_rent/item_details.html', {'item': item, 'form': form})
