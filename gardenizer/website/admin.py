from multiprocessing import Event
from django.contrib import admin
from account.models import Account
from event.models import Category,City,Customer,Evenement

# Register your models here.
admin.site.register(Account)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(Customer)
admin.site.register(Evenement)

class UserAdmin(admin.ModelAdmin):
    list_display = (
        "lastname",
        "firstname",
        "email",
    )