from django import forms


class ClientForm(forms.Form):
    name = forms.CharField(max_length=20, min_length=2)
    phone = forms.CharField(max_length=12, min_length=10)
