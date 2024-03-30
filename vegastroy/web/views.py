from django.shortcuts import render


def home(request):

    context = {

    }

    return render(request, 'web/home_login.html', context)


def custom_404(request, exception):
    return render(request, '404.html', status=404)