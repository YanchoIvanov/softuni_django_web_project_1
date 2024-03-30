from django import forms
from django.forms import ModelForm
from vegastroy.ask_for_offer.models import AskForOffer


class AskForOfferForm(ModelForm):
    class Meta:
        model = AskForOffer
        fields = '__all__'
        phone_number = forms.RegexField(
            regex=r'^\+?1?\d{9,15}$',
        )
