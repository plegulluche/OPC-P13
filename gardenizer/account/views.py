from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import (
logout, login, authenticate
)
from django.contrib.auth.decorators import login_required
from account.models import Account
from account.forms import (
    RegisterUserForm, AccountAuthenticationForm
)
from event.models import (
    City, Customer, Evenement
)


def registration_view(request ,*args, **kwargs):
    """
    View to register users and log them in uppon registration.
    """
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f'Vous etes déjà autentifié en tant que {user.email}')
    
    context = {}
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request,account)
            return redirect('mainpage')
        else:
            context['registration_form'] = form
    else:
        form = RegisterUserForm()
        context["registration_form"] = form
    return render(request, 'account/register.html',context)

    
def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('mainpage')
    if request.method == 'POST':
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email,password=password)
            if user:
                login(request,user)
                return redirect('mainpage')
    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form

    return render(request, 'account/login.html',context)

def logout_view(request):
    logout(request)
    return redirect('mainpage')

@login_required
def account_view(request):
    active_user = request.user.id
    all_events = Evenement.objects.filter(user=active_user)
    all_customers = Customer.objects.filter(user=active_user)
    cities = City.objects.all()
    context = {"events": all_events, "customers": all_customers,"cities":cities}
    
    return render(request, 'account/account.html', context)

@login_required
def account_customer_view(request):
    current_user = request.user.id
    customers = Customer.objects.filter(user=current_user)
    context = {"customers":customers}
    return render(request,"account/account_customers.html",context)

@login_required
def account_events_view(request):
    current_user = request.user.id
    events = Evenement.objects.filter(user=current_user)
    context = {"events":events}
    return render(request,"account/account_events.html",context)