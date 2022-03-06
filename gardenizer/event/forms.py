from django import forms
from account.models import Account
from event.models import Category, City, Customer, Evenement


class AddCustomerForm(forms.ModelForm):
    
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

            )
    
        
class AddEventForm(forms.ModelForm):
    
    class Meta:
        model = Evenement
        fields = '__all__'
    
    
        