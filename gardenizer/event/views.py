from lib2to3.pytree import convert
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Category,City,Customer,Evenement
from account.models import Account
from .forms import (
    AddCustomerForm, 
    AddMaintenanceEventForm,
    AddCustomerEventForm
)
from .management.commands.date_formater import (
    convert_string_to_date_time_object as cstdt,
    convert_date_object_to_string as cdtstr
)


@login_required
def add_maintenance_event_view(request):
    """
    View displaying a form to add events to the database with category:Entretient et révision matériel
    """
    context = {}
    
    if request.method == 'POST':
        form = AddMaintenanceEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            user = Account.objects.get(pk=request.user.id)
            category = Category.objects.get(title='Entretient et révision matériel')
            date_start = cstdt(request.POST.get('event_start'))
            date_end = cstdt(request.POST.get('event_end'))
            event.event_start = date_start
            event.event_end = date_end
            event.user = user
            event.category = category
            event.save()
            context['message'] = "Tâche d'entretient ajouté avec succès"
            return redirect('account_event')
        else:
            context['add_maintenance_form'] = form
            
    else:
        form = AddMaintenanceEventForm()
        context = {"add_maintenance_form":form}    
        return render(request, 'event/add_maintenance_event_form.html',context)


@login_required
def add_customer_event_view(request):
    """
    View displaying a form to add events to the database with category:Chantier
    """
    context = {}
    
    if request.method == 'POST':
        form = AddCustomerEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            user = Account.objects.get(pk=request.user.id)
            category = Category.objects.get(title='Chantier')
            date_start = cstdt(request.POST.get('event_start'))
            date_end = cstdt(request.POST.get('event_end'))
            event.event_start = date_start
            event.event_end = date_end
            event.user = user
            event.category = category
            event.save()
            context['message'] = "Tâche d'entretient ajouté avec succès"
            return redirect('account_event')
        else:
            context['add_event_form'] = form
            
    else:
        customers = Customer.objects.all()
        form = AddCustomerEventForm()
        context = {"add_event_form":form,'customers':customers}    
        return render(request, 'event/add_customer_event_form.html',context)
    
    
@login_required
def update_event_view(request,eventid):
    event = Evenement.objects.get(pk=eventid)
    customers = Customer.objects.all()

    if request.method == 'POST':
        form = form_type(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            date_start = cstdt(request.POST.get('event_start'))
            date_end = cstdt(request.POST.get('event_end'))
            event.event_start = date_start
            event.event_end = date_end
            event.save()
            context['message'] = 'Evènement édité avec succès'
            return redirect('account_event')
        else:
            context['update_event_form'] = form_type
    if event.category.title == 'Chantier':
        type = "chantier"
        start_date_str = cdtstr(event.event_start)
        end_date_str = cdtstr(event.event_end)
        form_type = AddCustomerEventForm()
        context = {"update_event_form":form_type,'event':event,'type':type,'customers':customers,'start':start_date_str,'end':end_date_str}
        return render(request, 'event/edit_event.html', context)
    else:
        type = ""
        start_date_str = cdtstr(event.event_start)
        end_date_str = cdtstr(event.event_end)
        form_type = AddMaintenanceEventForm()
        context = {"update_event_form":form_type,'event':event,'type':type,'start':start_date_str,'end':end_date_str} 
        return render(request, 'event/edit_event.html', context)



@login_required
def delete_event_view(request,eventid):
    """
    """
    event = Evenement.objects.get(pk=eventid)
    if request.method == 'POST':
        event.delete()
        return redirect('account_event')
    context ={"event":event}
    return render(request, "event/delete_event_confirmation.html",context)


@login_required
def add_customer_view(request):
    """
    View creating new customer from post data of a creation form
    """
    context = {}
    
    if request.method == 'POST':
        form = AddCustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            user = Account.objects.get(pk=user)
            customer.user = user
            customer.save()
            context['message'] = 'Client ajouté avec succès'
            return redirect('account_customer')
        else:
            context['add_customer_form'] = form
            
    else:
        form = AddCustomerForm()
        context = {"add_customer_form":form}    
        return render(request, 'event/add_customer.html',context)

@login_required
def delete_customer_view(request,customerid):
    """
    """
    customer = Customer.objects.get(pk=customerid)
    if request.method == 'POST':
        customer.delete()
        return redirect('account_customer')
    context = {"customer":customer}
    return render(request,'event/delete_customer_confirmation.html',context)

@login_required
def edit_customer_view(request,customerid):
    """
    """
    context = {}
    customer = Customer.objects.get(pk=customerid)
    if request.method == 'POST':
        form = AddCustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            context['message'] = 'Client édité avec succès'
            return redirect('account_customer')
        else:
            context['update_customer_form'] = form
    else:
        customer = Customer.objects.get(pk=customerid)
        form = AddCustomerForm(instance=customer)
        context = {"update_customer_form":form,'customer':customer} 
    return render(request, 'event/update_customer_form.html', context)