from django.contrib import admin
from account.models import Account

# Register your models here.
admin.site.register(Account)

class UserAdmin(admin.ModelAdmin):
    list_display = (
        "lastname",
        "firstname",
        "email",
    )