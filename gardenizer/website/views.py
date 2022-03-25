from django.shortcuts import render
from event.models import City


def mainpage(request):

    return render(request, "website/mainpage.html")