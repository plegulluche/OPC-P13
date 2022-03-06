from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Category,City,Customer,Evenement
from account.models import Account
from .forms import (
    AddCustomerForm
)


@login_required
def add_maintenance_event_view(request):
    """
    View displaying a form to add events to the database with category:Entretient et révision matériel
    """
    message = ""
    if request.method == 'POST':
        title = request.POST.get("title")
        start_date = request.POST.get("startdate")
        description = request.POST.get("description")
        if title != "":
            if start_date != "":
                if description != "":
                    new_event = Evenement()
                    new_event.title = title
                    new_event.event_start = start_date
                    new_event.description = description
                    new_event.user = Account.objects.get(pk=request.user.id)
                    category = Category.objects.filter(title="Entretient et révision matériel").first()
                    new_event.category = category
                    new_event.save()
                    message = "Nouvelle tache d'entretient enregistrée avec succès"
                else:
                    message = "Veuillez remplir tout les champs"
                    return render(request, "event/add_maintenance_event_form.html",{"message":message})
            else:
                message = "Veuillez remplir tout les champs"
                return render(request, "event/add_maintenance_event_form.html",{"message":message})
        else:
            message = "Veuillez remplir tout les champs"
            return render(request, "event/add_maintenance_event_form.html",{"message":message})
        
    return render(request, 'event/account_events.html',{"message":message})

@login_required
def add_customer_event_view(request):
    """
    View displaying a form to add events to the database with category:Chantier
    """
    message = ""
    if request.method == 'POST':
        title = request.POST.get("title")
        start_date = request.POST.get("startdate")
        end_date = request.POST.get("enddate")
        description = request.POST.get("description")
        customer_id = request.POST.get("customer")
        if end_date == "":
            end_date = None
        
        if title != "":
            if start_date is not None:
                if description != "":
                    if customer_id != "":
                        new_event = Evenement()
                        new_event.title = title
                        new_event.event_start = start_date
                        new_event.event_end = end_date
                        new_event.description = description
                        category = Category.objects.filter(title="Chantier").first()
                        new_event.category = category
                        new_event.user = Account.objects.get(pk=request.user.id)
                        new_event.customer = Customer.objects.get(pk=customer_id)
                        new_event.save()
                        message = "Chantier ajouté avec succès"
                        return redirect('account-event')
                    else:
                        message = "Veuillez selectionner un client ,si ce n'est pas déjà fait ajoutez en un via le formulaire correspondant"
                        return render(request, "event/add_customer_event_form.html",context)
                else:
                    message = "Veuillez saisir tout les champs"
                    return render(request, "event/add_customer_event_form.html",context)
            else:
                message = "Veuillez saisir tout les champs"
                return render(request, "event/add_customer_event_form.html",context)
        else:
            message = "Veuillez saisir tout les champs"
            return render(request, "event/add_customer_event_form.html",context)
    
    customers = Customer.objects.all()
    categories = Category.objects.all()
    cities = City.objects.all()
    context = {"categories":categories, "cities":cities, "message":message,"customers":customers}
    
    return render(request, "event/add_customer_event_form.html",context)

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
def update_event_view(request,eventid):
    """
    """
    pass

