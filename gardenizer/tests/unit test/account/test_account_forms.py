import pytest
from account.models import Account
from account.forms import AccountAuthenticationForm,RegisterUserForm

# def test_yes_register_user_form():
#     data = {
#         'email':'testuser@gmail.com',
#         'username':'testuser',
#         'password1':'Xqjrqp8800',
#         'password2':'Xqjrqp8800'
#     }
#     form = RegisterUserForm(data)
#     assert form.is_valid() == True


# def test_no_account_auth_form():
#     data = {
#         "email": "testuser@gmail",
#         "password": "13456"
#     }
#     form = AccountAuthenticationForm(data)
#     assert form.is_valid() == False
    
# @pytest.mark.parametrize(
#     'email , password, validity',
#     [
#         ('testuser@gmail.com', 'password', True),
#         ('testuser@', 'password', False),
#         ('testuser@gmail.com', '', False)
#     ]
# )
# def test_account_auth_form(email,password,validity):
#     form = AccountAuthenticationForm(data={
#         'email':email,
#         'password':password,
#     })
#     assert form.is_valid() is validity

    