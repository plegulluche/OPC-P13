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
    
        
class AddMaintenanceEventForm(forms.ModelForm):
    
    event_start = forms.DateTimeField()
    event_end = forms.DateTimeField()
    
    class Meta:
        model = Evenement
        fields = (
            'title',
            'description',
            )
        
class AddCustomerEventForm(forms.ModelForm):
    
    class Meta:
        model = Evenement
        fields = (
            'title',
            'description',
            'customer',
            )
    
    
        