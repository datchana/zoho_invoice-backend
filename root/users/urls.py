from django.urls import path

from users.views import SignupView, SignInView, InvoiceView, ContactsPersonView, CustomerView

urlpatterns = [
     path("contacts/signup", SignupView.as_view(), name="signup"),
     path("contacts/signin", SignInView.as_view(), name="signin"),
     path("invoice/manage", InvoiceView.as_view(), name="invoice" ),
     path("contact-person/manage", ContactsPersonView.as_view(), name="contact_person" ),
     path("customer/manage", CustomerView.as_view(), name="customer" ),
]