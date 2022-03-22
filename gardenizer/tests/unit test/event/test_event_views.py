import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from event.models import Customer, Evenement

@pytest.mark.django_db
def test_event_add_maintenance_view_form_valid(
    client,
    authenticated_user,
    yes_add_maintenance_event_form_data,
    create_categories):
    """test valid post data on add maintenance event view"""
    response = client.post('/add-maintenance-event',data=yes_add_maintenance_event_form_data)
    assert response.status_code == 302
    assertTemplateUsed('event/add_maintenance_event_form.html')

@pytest.mark.django_db
def test_event_add_maintenance_view_form_not_valid(
    client,
    authenticated_user,
    create_categories,
    no_add_maintenance_event_form_data
    ):
    """test invalid post data on add maintenance event view"""
    response = client.post('/add-maintenance-event',data=no_add_maintenance_event_form_data)
    assert 'add_maintenance_form' in response.context

@pytest.mark.django_db
def test_event_add_maintenance_view_get(client,authenticated_user):
    """test the get method on add maintenance event view"""
    response = client.get('/add-maintenance-event')
    assert response.status_code == 200
    assert 'add_maintenance_form' in response.context
    assertTemplateUsed('event/add_maintenance_event_form.html')
    

@pytest.mark.django_db
def test_get_add_customer_event_view(client,authenticated_user):
    """test get method for add customer event view"""
    response = client.get('/add-customer-event')
    assert response.status_code == 200
    assertTemplateUsed('event/add_customer_event_form.html')
    
@pytest.mark.django_db
def test_valid_post_data_add_customer_event(
    client,
    authenticated_user,
    create_categories,
    yes_add_customer_event_form_data,
    create_customer
):
    """test valid post data on add customer event view"""
    response = client.post('/add-customer-event',data=yes_add_customer_event_form_data)
    assert response.status_code == 302
    
@pytest.mark.django_db
def test_invalid_post_data_add_customer_event(
    client,
    authenticated_user,
    create_categories,
    no_add_customer_event_form_data,
    create_customer
):
    """test invalid post data on add customer event view"""
    response = client.post('/add-customer-event',data=no_add_customer_event_form_data)
    assert response.status_code == 200
    assert 'add_event_form' in response.context
    
@pytest.mark.django_db
def test_get_update_customer_event_view(
    client,
    authenticated_user,
    create_maintenance_event
    ):
    """test the get method for the update customer event view"""
    event = Evenement.objects.all()
    response = client.get(reverse('update_customer_event',kwargs={'eventid':event[0].id}))
    assert response.status_code == 200
    assertTemplateUsed('event/edit_event.html')

@pytest.mark.django_db
def test_post_update_customer_event_view(
    client,
    authenticated_user,
    create_maintenance_event
):
    """test the post method on customer event view"""
    event = Evenement.objects.all()
    payload = {
        'title':"another title",
        'event_start':"2022-03-09T10:45",
        'event_end':"2022-03-09T10:45",
    }
    response = client.post(reverse('update_customer_event',kwargs={'eventid':event[0].id}),data=payload)
    assert response.status_code == 302
    assertTemplateUsed('event/update_success.html')
    
@pytest.mark.django_db
def test_get_method_update_maintenance_event_view(
    client,
    authenticated_user,
    create_customer_event
    ):
    """test the get method for update maintenance event view"""
    event = Evenement.objects.all()
    response = client.get(reverse('update_maintenance_event',kwargs={'eventid':event[0].id}))
    assert response.status_code == 200
    assertTemplateUsed('event/edit_event.html')
    
@pytest.mark.django_db
def test_post_customer_event_view(
    client,
    authenticated_user,
    create_maintenance_event
):
    """test the post method on maintenance event view"""
    event = Evenement.objects.all()
    payload = {
        'title':"another title",
        'event_start':"2022-03-09T10:45",
        'event_end':"2022-03-09T10:45",
    }
    response = client.post(reverse('update_maintenance_event',kwargs={'eventid':event[0].id}),data=payload)
    assert response.status_code == 302
    

def test_get_update_success_view(client):
    """test the get method of success update event view"""
    response = client.get('/success')
    assert response.status_code == 200
    assertTemplateUsed('event/update_success.html')
    
@pytest.mark.django_db
def test_delete_event_view(
    client,
    authenticated_user,
    create_maintenance_event):
    """test the get method of the delete event view"""
    event = Evenement.objects.all()
    response = client.get(reverse('delete_event',kwargs={'eventid':event[0].id}))
    assert response.status_code == 200
    assertTemplateUsed('event/delete_event_confirmation.html')
    
@pytest.mark.django_db
def test_post_delete_event_view(
    client,
    authenticated_user,
    create_maintenance_event):
    """test the post method of the delete event view"""
    event = Evenement.objects.all()
    response = client.post(reverse('delete_event',kwargs={'eventid':event[0].id}))
    assert response.status_code == 302
    assertTemplateUsed('account/account_event.html')
    
@pytest.mark.django_db
def test_get_method_add_customer_view(
    client,
    authenticated_user,
):
    """Test get method of add customer view"""
    response = client.get('/add-customer')
    assert response.status_code == 200
    assert 'add_customer_form' in response.context
    assertTemplateUsed('event/add_customer.html')
    
@pytest.mark.django_db
def test_valid_post_method_add_customer_view(
    client,
    authenticated_user,
    yes_add_customer_form_data
):
    """test the post method with valid post data of the add customer _view"""
    response = client.post('/add-customer',data=yes_add_customer_form_data)
    assert response.status_code == 302
    assertTemplateUsed('account/account_customers.html')

@pytest.mark.django_db
def test_invalid_post_method_add_customer_view(
    client,
    authenticated_user,
    no_add_customer_form_data
):
    """test the post method with invalid post data of the add customer _view"""
    response = client.post('/add-customer',data=no_add_customer_form_data)
    assert response.status_code == 200
    assertTemplateUsed('event/add_customer.html')
    assert "add_customer_form" in response.context

@pytest.mark.django_db
def test_get_delete_customer_view(
    client,
    authenticated_user,
    create_customer
):
    """test the get method of the delete customer view"""
    customer = Customer.objects.all()
    response = client.get(reverse('customer_delete',kwargs={'customerid':customer[0].id}))
    assert response.status_code == 200
    assertTemplateUsed('event/delete_customer_confirmation.html')
    
    
@pytest.mark.django_db
def test_post_delete_customer_view(
    client,
    authenticated_user,
    create_customer):
    """test the post method of the delete customer view"""
    customer = Customer.objects.all()
    response = client.post(reverse('customer_delete',kwargs={'customerid':customer[0].id}))
    assert response.status_code == 302
    assertTemplateUsed('account/account_customers.html')
    
@pytest.mark.django_db
def test_get_method_edit_customer_view(
    client,
    authenticated_user,
    create_customer
):
    """test the get method for the edit customer view"""
    customer = Customer.objects.all()
    response = client.get(reverse('customer_update',kwargs={'customerid':customer[0].id}))
    assert response.status_code == 200
    assertTemplateUsed('event/update_customer_form.html')
    
@pytest.mark.django_db
def test_valid_post_edit_customer_view(
    client,
    authenticated_user,
    create_customer,
    create_city
):
    """test valid post data for the post method of the edit customer view"""
    customer = Customer.objects.all()
    payload = {
        'firstname':'customer',
        'lastname':'lastname',
        'phone':'066666655',
        'company':'fakecompany',
        'street_number':'125',
        'streetname':'une rue',
        'city':create_city.id
    }
    response = client.post(reverse('customer_update',kwargs={'customerid':customer[0].id}),data=payload)
    assert response.status_code == 302
    
@pytest.mark.django_db
def test_invalid_post_edit_customer_view(
    client,
    authenticated_user,
    create_customer,
):
    """test invalid post data for the post method of edit customer view """
    customer = Customer.objects.all()
    payload = {
        'firstname':'customer',
        'lastname':'lastname',
        'phone':'066666655',
        'company':'fakecompany',
        'street_number':'125',
        'streetname':'une rue',
        
    }
    response = client.post(reverse('customer_update',kwargs={'customerid':customer[0].id}),data=payload)
    assert response.status_code == 200
    assert 'update_customer_form' in response.context