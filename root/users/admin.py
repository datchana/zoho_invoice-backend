from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Contacts, Address, ContactPersons, Customer, Invoice

# Register your models here.


class UserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
    )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        (
            "Additional info",
            {
                "fields": (
                    "contact_name",
                    "phnumber",
                    "company_name",
                    "address",
                )
            },
        ),
    )

class AddressAdmin(admin.ModelAdmin):
    search_fields = ['attention',]
    list_display = ['attention']

class ContactPersonsAdmin(admin.ModelAdmin):
    search_fields = ['contacts',]
    list_display = ['contacts']

class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['name',]
    list_display = ['name']

class InvoiceAdmin(admin.ModelAdmin):
    search_fields = ['invoice_number',]
    list_display = ['invoice_number']


admin.site.register(Contacts, UserAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(ContactPersons, ContactPersonsAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Invoice, InvoiceAdmin)