from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

# Create your models here.

class Address(models.Model):
    ADDRESSES_CHOICES = (
    ("billing_address", "billing_address"),
    ("shipping_address", "shipping_address"),
    ("customer_address", "customer_address"),
    )
    attention = models.CharField(max_length=100, default="")
    address = models.CharField(max_length=500, default="")
    street2 = models.CharField(max_length=100, default="")
    state_code = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=50, default="")
    zip_code = models.CharField(max_length=50, default="")
    country = CountryField()
    fax = models.CharField(max_length=100, default="")
    address_type = models.CharField(
        max_length = 20,
        choices = ADDRESSES_CHOICES,
        default = 'billing_address'
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.attention


class Contacts(AbstractUser):
    contact_name = models.CharField(max_length=100, default="")
    phnumber = PhoneNumberField(default="")
    company_name = models.CharField(max_length=50, default="")
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ContactPersons(models.Model):
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE, default=None, null=True)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    email = models.EmailField(default="")
    skype = models.CharField(max_length=50, default="")
    department = models.CharField(max_length=50, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    name = models.CharField(max_length=100, default="")
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default=None, null=True)
    phnumber = PhoneNumberField(default="")
    email = models.EmailField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Invoice(models.Model):
    INVOICE_STATUS_CHOICES = (
    ("sent", "sent"),
    ("draft", "draft"),
    ("overdue", "overdue"),
    ("paid", "paid"),
    ("void", "void"),
    ("unpaid", "unpaid"),
    ("partially_paid", "partially_paid"),
    ("viewed", "viewed"),
    )

    CURRENCY_CODES_CHOICES = (
    ("CZK", "CZK"),
    ("EUR", "EUR"),
    ("INR", "INR"),
    ("HRK", "HRK"),
    ("HUF", "HUF"),
    ("RON", "RON"),
    ("USD", "USD"),
    )


    invoice_number = models.CharField(max_length=100, default="")
    
    # Need to create reccuring invoice model
    # recurring_invoice_id 
    search_text = models.CharField(max_length=20, default="")
    sort_column = models.CharField(max_length=50, default="")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default="")
    status = models.CharField(
        max_length = 20,
        choices = INVOICE_STATUS_CHOICES,
        default = 'draft'
        )
    date =  models.DateTimeField(default="")
    due_date =  models.DateTimeField(default="")
    due_days = models.IntegerField()
    currency_code = models.CharField(
        max_length = 20,
        choices = CURRENCY_CODES_CHOICES,
        default = 'INR'
        )
    total  = models.FloatField()
    balance  = models.FloatField()
    is_emailed = models.BooleanField(default=False)
    reminders_sent = models.IntegerField()
    payment_expected_date = models.DateTimeField(default="")
    last_payment_date = models.DateTimeField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

