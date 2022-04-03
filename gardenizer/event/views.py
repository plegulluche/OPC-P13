from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, City, Customer, Evenement
from account.models import Account
from .forms import AddCustomerForm, AddMaintenanceEventForm, AddCustomerEventForm
from .utils import (
    convert_string_to_date_time_object as cstdt,
)


@login_required
def add_maintenance_event_view(request):
    """
    View displaying a form to add events to the database with category:Entretient et révision matériel
    """
    context = {}

    if request.method == "POST":
        form = AddMaintenanceEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            user = Account.objects.get(pk=request.user.id)
            category = Category.objects.get(title="Entretient et révision matériel")
            date_start = cstdt(request.POST.get("event_start"))
            date_end = cstdt(request.POST.get("event_end"))
            event.event_start = date_start
            event.event_end = date_end
            event.user = user
            event.category = category
            event.save()
            context["message"] = "Tâche d'entretient ajouté avec succès"
            return redirect("account_event")
        else:
            context["add_maintenance_form"] = form

    else:
        form = AddMaintenanceEventForm()
        context = {"add_maintenance_form": form}
    return render(request, "event/add_maintenance_event_form.html", context)


@login_required
def add_customer_event_view(request):
    """
    View displaying a form to add events to the database with category:Chantier
    """
    context = {}

    if request.method == "POST":
        form = AddCustomerEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            user = Account.objects.get(pk=request.user.id)
            category = Category.objects.get(title="Chantier")
            date_start = cstdt(request.POST.get("event_start"))
            date_end = cstdt(request.POST.get("event_end"))
            event.event_start = date_start
            event.event_end = date_end
            event.user = user
            event.category = category
            event.save()
            context["message"] = "Tâche d'entretient ajouté avec succès"
            return redirect("account_event")
        else:
            context["add_event_form"] = form

    else:
        user = Account.objects.get(pk=request.user.id)
        customers = Customer.objects.filter(user=user).all()
        form = AddCustomerEventForm()
        context = {"add_event_form": form, "customers": customers}
    return render(request, "event/add_customer_event_form.html", context)


@login_required
def update_customer_event_view(request, eventid):
    """
    View that display the AddCustomerEventForm filled with that customer
    infos and allows the user to modify it.
    """
    context = {}
    event = Evenement.objects.get(pk=eventid)
    type = "chantier"
    customers = Customer.objects.filter(user=request.user.id)
    form = AddCustomerEventForm(request.POST or None, instance=event)
    message = ""
    if form.is_valid():
        event = form.save(commit=False)
        event.event_start = cstdt(request.POST.get("event_start"))
        event.event_end = cstdt(request.POST.get("event_end"))
        event.save()
        return redirect("success")
    else:
        context["form"] = form
        context["message"] = "Veuillez remplir tout les champs"
    context = {
        "event": event,
        "form": form,
        "message": message,
        "type": type,
        "customers": customers,
    }
    return render(request, "event/edit_event.html", context)


@login_required
def update_maintenance_event_view(request, eventid):
    """
    View that display the AddMaintenanceEventForm with an event infos
    and allow the corresponding user to modify the datas of that event
    """
    context = {}
    event = Evenement.objects.get(pk=eventid)
    form = AddMaintenanceEventForm(request.POST or None, instance=event)
    message = ""
    if form.is_valid():
        event = form.save(commit=False)
        event.event_start = cstdt(request.POST.get("event_start"))
        event.event_end = cstdt(request.POST.get("event_end"))
        event.save()
        return redirect("success")
    else:
        context["form"] = form
        context["message"] = "Veuillez remplir tout les champs"
    context = {"event": event, "form": form, "message": message}
    return render(request, "event/edit_event.html", context)


def render_update_success_page(request):
    """
    Display a success message after a user used the form to update
    an event or a customer.
    """
    return render(request, "event/update_success.html")


@login_required
def delete_event_view(request, eventid):
    """
    View that allow a user to delete an event.
    """
    event = Evenement.objects.get(pk=eventid)
    if request.method == "POST":
        event.delete()
        return redirect("account_event")
    context = {"event": event}
    return render(request, "event/delete_event_confirmation.html", context)


@login_required
def add_customer_view(request):
    """
    View creating new customer from post data with AddCustomerForm
    """
    cities = City.objects.all()
    context = {}

    if request.method == "POST":
        form = AddCustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            user = Account.objects.get(pk=request.user.id)
            customer.user = user
            customer.save()
            return redirect("account_customer")
        else:
            context["add_customer_form"] = form

    else:
        form = AddCustomerForm()
        context = {"add_customer_form": form, "cities": cities}
    return render(request, "event/add_customer.html", context)


@login_required
def delete_customer_view(request, customerid):
    """
    View that allow a user to delete a customer.
    """
    customer = Customer.objects.get(pk=customerid)
    if request.method == "POST":
        customer.delete()
        return redirect("account_customer")
    context = {"customer": customer}
    return render(request, "event/delete_customer_confirmation.html", context)


@login_required
def edit_customer_view(request, customerid):
    """
    View that allow a user to edit datas of a customer with a
    pre-filled AddCustomerForm with customer datas.
    """
    context = {}
    customer = Customer.objects.get(pk=customerid)
    if request.method == "POST":
        form = AddCustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            context["message"] = "Client édité avec succès"
            return redirect("account_customer")
        else:
            context["update_customer_form"] = form
    else:
        customer = Customer.objects.get(pk=customerid)
        form = AddCustomerForm(instance=customer)
        context = {"update_customer_form": form, "customer": customer}
    return render(request, "event/update_customer_form.html", context)
