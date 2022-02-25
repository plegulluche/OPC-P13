from sre_parse import CATEGORIES
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Category,City,Customer,Evenement
from account.models import Account


@login_required
def select_event_type_view(request):
    """
    Display a menu for events types and redirect to the form corresponding to that type.
    """
    if request.method == 'POST':
        category_id = request.POST.get("category")
        category = Category.objects.get(pk=int(category_id))
        if category.title == "Entretient et révision matériel":
            return redirect("add_maintenance_event")
        elif category.title == "Chantier":
            return redirect("add_customer_event")
        
    categories = Category.objects.all()
    context = {"categories":categories}
    
    return render(request, 'event/event_selector.html',context)

@login_required
def add_maintenance_event_view(request):
    """
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
                    category = Category.objects.filter(title="Entretient et révision matériel").first()
                    new_event.category = category
                    new_event.save()
                else:
                    message = "Veuillez remplir tout les champs"
                    return render(request, "event/add_maintenance_event_form.html",{"message":message})
            else:
                message = "Veuillez remplir tout les champs"
                return render(request, "event/add_maintenance_event_form.html",{"message":message})
        else:
            message = "Veuillez remplir tout les champs"
            return render(request, "event/add_maintenance_event_form.html",{"message":message})
        
    return render(request, 'event/add_maintenance_event_form.html',{"message":message})

@login_required
def add_customer_event_view(request):
    """
    View displaying a form to add events to the database.
    """
    message = ""
    if request.method == 'POST':
        title = request.POST.get("title")
        start_date = request.POST.get("startdate")
        end_date = request.POST.get("enddate")
        description = request.POST.get("description")
        category_id = request.POST.get("category")
        customer_id = request.POST.get("customer")
        
        if title != "":
            if start_date is not None:
                if description != "":
                    if customer_id != "":
                        new_event = Evenement()
                        new_event.title = title
                        new_event.event_start = start_date
                        new_event.event_end = end_date
                        new_event.description = description
                        new_event.category = Category.objects.get(id=int(category_id))
                        new_event.user = Account.objects.get(pk=request.user.id)
                        new_event.customer = Customer.objects.get(pk=customer_id)
                        new_event.save()
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
    message = ""
    if request.method == "POST":
        current_user_id = request.user.id
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        phone = request.POST.get("phone")
        company = request.POST.get("company")
        city_id = request.POST.get("city")
        street_number = request.POST.get("number")
        street_name = request.POST.get("streetname")
        
        if firstname != "":
            if lastname != "":
                if street_name != "":
                    if street_number != "":
                        if city_id != "":
                            new_customer = Customer()
                            new_customer.firstname = firstname
                            new_customer.lastname = lastname
                            new_customer.phone = phone
                            new_customer.company = company
                            new_customer.streetname = street_name
                            new_customer.street_number = street_number
                            new_customer.city = City.objects.get(id=int(city_id))
                            new_customer.user = Account.objects.get(pk=current_user_id)
                            new_customer.save()
                        else:
                            message = "Veuillez saisir tout les champs"
                            return render(request, 'event/add_customer.html',context)
                    else:
                        message = "Veuillez saisir tout les champs"
                        return render(request, 'event/add_customer.html',context)
                else:
                    message = "Veuillez saisir tout les champs"
                    return render(request, 'event/add_customer.html',context)
            else:
                message = "Veuillez saisir tout les champs"
                return render(request, 'event/add_customer.html',context)
        else:
            message = "Veuillez saisir tout les champs"
            return render(request, 'event/add_customer.html',context)
        
    all_cities = City.objects.all()
    context = {"message":message,"cities":all_cities}
        
    return render(request, 'event/add_customer.html',context)