from django import forms

from .models import Address

class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ('name', 'call_1', 'call_2', 'e_mail',)

