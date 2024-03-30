from django.urls import path

from vegastroy.ask_for_offer.views import ask_for_offer, success

urlpatterns = [
    path('', ask_for_offer, name='contact_form_offer'),
    path('success/', success, name='success')

]
