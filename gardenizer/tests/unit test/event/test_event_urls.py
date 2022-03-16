from django.urls import reverse, resolve

def test_add_customer():
    path = reverse("add_customer_event")
    assert path == "/add-customer-event"
    assert resolve(path).view_name == "add_customer_event"
    
def test_add_maintenance():
    path = reverse("add_maintenance_event")
    assert path == "/add-maintenance-event"
    assert resolve(path).view_name == "add_maintenance_event"

def event_delete():
    path = reverse('delete_event',kwargs={"eventid":1})
    assert path == "/event/1/delete"
    assert resolve(path).view_name == "delete_event"
    
def update_customer_event():
    path = reverse('update_customer_event',kwargs={"eventid":1})
    assert path == "/customer-event/1/update"
    assert resolve(path).view_name == "update_customer_event"
    
def maintenance_event_update():
    path = reverse('update_maintenance_event',kwargs={"eventid":1})
    assert path == '/maintenance-event/1/update'
    assert resolve(path).view_name == "update_maintenance_event"
    
def add_customer():
    path = reverse('add_customer')
    assert path == '/add-customer'
    assert resolve(path).view_name == "add_customer"
    
def customer_delete():
    path = reverse('customer_delete',kwargs={'customerid':1})
    assert path == '/customer/1/delete'
    assert resolve(path).view_name == 'customer_delete'
    
def customer_update():
    path = reverse('customer_update',kwargs={'customerid':1})
    assert path == '/customer/1/update'
    assert resolve(path).view_name == 'customer_update'
    
def success():
    path = reverse('success')
    assert path == "/success"
    assert resolve(path).view_name == 'success'
    

    
    
