from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from account.models import Account


def registration_view(request):
    """View managing the user creation"""
    
    message = ''
    if request.method == 'POST':
        username = request.POST.get("username")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_exists = Account.objects.filter(email=email).first()
        username_exists = Account.objects.filter(username=username).first()
        if user_exists:
            message = "cet email est déjà utilisé"
            return render(request, "account/register.html", {"message": message})
        if username_exists:
            message = "ce pseudo est déjà pris"
            return render(request, "account/register.html", {"message": message})
        if email != "":
            if password != "":
                if firstname != "":
                    if lastname != "":   
                        new_user = Account()
                        new_user.email = email
                        new_user.username = username
                        new_user.firstname = firstname
                        new_user.lastname = lastname
                        new_user.password = password
                        new_user.save()
                        new_user.set_password(password)
                        new_user.save()
                    else:
                        message = "Veuillez saisir tout les champs"
                        return render(request, "account/register.html", {"message": message})
                else:
                    message = "Veuillez saisir tout les champs"
                    return render(request, "account/register.html", {"message": message})
            else:
                message = "Veuillez saisir tout les champs"
                return render(request, "account/register.html", {"message": message})
        else:
            message = "Veuillez saisir tout les champs"
            return render(request, "account/register.html", {"message": message})
    
    return render(request, 'account/register.html')    

def login_view(request):
    message = ""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = Account.objects.filter(email=email).first()
        if user:
            utlisateur_auth = authenticate(email=user.email, password=password)
            if utlisateur_auth:
                login(request, utlisateur_auth)
                return redirect("mainpage")
            else:
                message = "vos identifiants ne sont pas corrects"
        else:
            message = "aucun utilisateur ne correspond a ces informations"
    
    return render(request, "account/login.html", {"message": message})

def logout_view(request):
    logout(request)
    return redirect('mainpage')