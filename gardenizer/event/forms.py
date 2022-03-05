from django import forms
from event.models import Evenement,Category,City,Customer
from account.models import Account


class AddCustomerForm(forms.ModelForm):
    
    phone = forms.CharField(max_length=25, help_text='ce champ est requis',required=True)
    street_number = forms.CharField(max_length=5,required=True)
    streetname = forms.CharField(max_length=150,required=True)
    
    class Meta:
        model = Customer
        fields = (
            'firstname',
            'lastname',
            'phone',
            'company',
            'street_number',
            'streetname',
            'city',
            'user',
            )
        