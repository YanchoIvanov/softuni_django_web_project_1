from django.shortcuts import render


def contacts_page(request):

    context = {

    }

    return render(request, 'contacts/contacts.html', context)
