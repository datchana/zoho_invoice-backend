from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
import hashlib
import random
from .models import Invoice, ContactPersons, Customer
from .settings import USER_CANCEL_SERIALIZER_ERROR_MSG

class UserSignupSerializer(serializers.ModelSerializer):
    """
    Serializer for User Signup endpoint.
    """

    client_id = serializers.CharField(max_length=100, required=True)
    client_secret = serializers.CharField(max_length=200, required=True)

    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "client_id",
            "client_secret",
        ]

    def validate_email(self, email):
        """
        Function to check user already exists
        """
        try:
            user = get_user_model().objects.get(email=email)
            if user:
                raise serializers.ValidationError("User already exists")
        except ObjectDoesNotExist:
            pass
        return email

    def create(self, validated_data):
        validated_data.pop("client_id", None)
        validated_data.pop("client_secret", None)
        validated_data["username"] = hashlib.sha1(
            str(random.random()).encode("utf-8")
        ).hexdigest()[:5]
        user = get_user_model().objects.create_user(**validated_data)
        return user


class UserSigninSerializer(serializers.Serializer):
    """
    Serializer for User Signin endpoint.
    """

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    client_id = serializers.CharField(max_length=100, required=True)
    client_secret = serializers.CharField(max_length=200, required=True)

    def validate(self, attrs):
        # validate existing user
        user = get_user_model().objects.filter(
            Q(username=attrs["username"]) | Q(email=attrs["username"])
        )
        attrs["is_existing_user"] = user.exists()
        if user.exists() and user.first().is_active == False:
            raise serializers.ValidationError(USER_CANCEL_SERIALIZER_ERROR_MSG)
        return attrs


class InvoiceSerializer(serializers.ModelSerializer):
    """
    Serializer for Invoice management endpoint.
    """
    class Meta:
        model = Invoice
        fields = '__all__'

class ContactsPersonSerializer(serializers.ModelSerializer):
    """
    Serializer for ContactsPersons management endpoint.
    """
    class Meta:
        model = ContactPersons
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializer for ContactsPersons management endpoint.
    """
    class Meta:
        model = Customer
        fields = '__all__'