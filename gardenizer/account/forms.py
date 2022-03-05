from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account

class RegisterUserForm(UserCreationForm):
    
    email = forms.EmailField(max_length=255, help_text="Requis. Ajouter une adresse email valide.(cet email est utilisé pour la récupération de votre mot de passe.)")
    
    class Meta:
        model = Account
        fields = ["email","username","password1","password2"]
    
    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        try:
            account = Account.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f'Cet email: {email} ,est déjà utilisé.')
    
    def clean_username(self):
        username = self.cleaned_data["username"].lower()
        try:
            account = Account.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f'Le pseudo: {username} ,est déjà utilisé.')
    
class AccountAuthenticationForm(forms.ModelForm):
    
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    
    class Meta:
        model = Account
        fields = ('email', 'password')
        
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            user = Account.objects.filter(email=email).first()
            if not authenticate(email=email,password=password):
                if not user:
                    raise forms.ValidationError("Cet utilisateur n'existe pas")
                else:
                    raise forms.ValidationError('Identifiants incorrects')
            
