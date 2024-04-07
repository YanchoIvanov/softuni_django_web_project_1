from django import forms


class AvailabilityRequestForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
