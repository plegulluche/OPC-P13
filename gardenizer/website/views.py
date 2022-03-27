from django.shortcuts import render
from event.models import City


def mainpage(request):
    return render(request, "website/mainpage.html")

def about_page_view(request):
    return render(request,"website/about.html")

def legals_page_view(request):
    return render(request,"website/legals.html")