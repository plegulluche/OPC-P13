from django.shortcuts import render


def mainpage(request):
    return render(request, "website/mainpage.html")


def about_page_view(request):
    return render(request, "website/about.html")


def legals_page_view(request):
    return render(request, "website/legals.html")


def handle_not_found(request, exception):
    return render(request, "website/not-found.html")
