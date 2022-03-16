from django.urls import reverse, resolve


def test_register():
    path = reverse("register")
    assert path == "/register/"
    assert resolve(path).view_name == "register"
    
def test_login():
    path = reverse('login')
    assert path == "/login/"
    assert resolve(path).view_name == "login"
    
def test_logout():
    path = reverse('logout')
    assert path == "/logout/"
    assert resolve(path).view_name == "logout"
    
def test_account():
    path = reverse('account')
    assert path == "/account"
    assert resolve(path).view_name == "account"

def test_account_customer():
    path = reverse('account_customer')
    assert path == "/account-customer"
    assert resolve(path).view_name == "account_customer"
    
def test_logout():
    path = reverse('account_event')
    assert path == "/account-event"
    assert resolve(path).view_name == "account_event"