from django.shortcuts import render
from .models import Category, City, Evenement
from account.models import Account

def add_event_view(request):
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
        city_id = request.POST.get("city")
        
        new_event = Evenement()
        new_event.title = title
        new_event.event_start = start_date
        new_event.event_end = end_date
        new_event.description = description
        new_event.category = Category.objects.get(id=int(category_id))
        new_event.city = City.objects.get(id=int(city_id))
        new_event.user = Account.objects.get(pk=request.user.id)
        new_event.save()
    
    categories = Category.objects.all()
    cities = City.objects.all()
    context = {"categories":categories, "cities":cities}
    
    return render(request, "event/add_event_form.html",context)