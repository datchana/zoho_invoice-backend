from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserSignupSerializer, UserSigninSerializer, InvoiceSerializer, ContactsPersonSerializer, CustomerSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .utils import get_token_info
from root.response import GenericResponse
from rest_framework import generics, status, permissions


# Create your views here.

class SignupView(GenericAPIView):
    """
    View for User Signup endpoint.
    """

    serializer_class = UserSignupSerializer
    permission_classes = [
        AllowAny,
    ]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            request_data = request.data
            client_id = request_data["client_id"]
            client_secret = request_data["client_secret"]
            user_data = serializer.save()
            token_info = get_token_info(
                        request,
                        user_data.username,
                        request_data.get("password"),
                        client_id,
                        client_secret,
                    )
            return GenericResponse(
                        success_msg="User create Successfully",
                        status=status.HTTP_201_CREATED,
                        data=token_info,
                    )
        else:
                return GenericResponse(
                    error_msg=serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )

class SignInView(GenericAPIView):
    """
    View for User Signin endpoint.
    """

    serializer_class = UserSigninSerializer
    permission_classes = [
        AllowAny,
    ]


    def post(self, request, *args, **kwargs):
        error_msg = {}
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                    user = get_user_model().objects.get(
                        email=request_data.get("username")
                    )
            except ObjectDoesNotExist:
                return GenericResponse(
                    error_msg=USER_DOEST_NOT_EXIST,
                    status=status.HTTP_400_BAD_REQUEST,
                )
            token_info = get_token_info(
            request,
            user.username,
            request_data.get("password"),
            client_id,
            client_secret,
            )
            if "error" in token_info:
                return GenericResponse(
                    error_msg=token_info, status=status.HTTP_400_BAD_REQUEST
                )
            return GenericResponse(
                    success_msg="User Logged In Successfully",
                    status=status.HTTP_200_OK,
                    data=token_info,
                )
        else:
            return GenericResponse(
                error_msg=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


class InvoiceView(GenericAPIView):
    serializer_class = InvoiceSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializers.save()
            return GenericResponse(
                        success_msg="Invoice created Successfully",
                        status=status.HTTP_200_OK,
                    )
        else:
            return GenericResponse(
                error_msg=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return GenericResponse(
                        data=serializer.data,
                        status=status.HTTP_200_OK,
                    )
        else:
            return GenericResponse(
                error_msg=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.update()
            return GenericResponse(
                        success_msg="Invoice updated Successfully",
                        status=status.HTTP_200_OK,
                    )
        else:
            return GenericResponse(
                error_msg=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
    def delete(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.delete()
            return GenericResponse(
                        success_msg="Invoice deleted Successfully",
                        status=status.HTTP_200_OK,
                    )
        else:
            return GenericResponse(
                error_msg=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

class ContactsPersonView(GenericAPIView):
    serializer_class = ContactsPersonSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializers.save()
            return GenericResponse(
                        success_msg="ContactsPerson created Successfully",
                        status=status.HTTP_200_OK,
                    )
        else:
            return GenericResponse(
                error_msg=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return GenericResponse(
                        data=serializer.data,
                        status=status.HTTP_200_OK,
                    )
        else:
            return GenericResponse(
                error_msg=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.update()
            return GenericResponse(
                        success_msg="ContactsPerson updated Successfully",
                        status=status.HTTP_200_OK,
                    )
        else:
            return GenericResponse(
                error_msg=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
    def delete(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.delete()
            return GenericResponse(
                        success_msg="ContactsPerson deleted Successfully",
                        status=status.HTTP_200_OK,
                    )
        else:
            return GenericResponse(
                error_msg=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

class CustomerView(GenericAPIView):
    serializer_class = CustomerSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializers.save()
            return GenericResponse(
                        success_msg="ContactsPerson created Successfully",
                        status=status.HTTP_200_OK,
                    )
        else:
            return GenericResponse(
                error_msg=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return GenericResponse(
                        data=serializer.data,
                        status=status.HTTP_200_OK,
                    )
        else:
            return GenericResponse(
                error_msg=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.update()
            return GenericResponse(
                        success_msg="Customer updated Successfully",
                        status=status.HTTP_200_OK,
                    )
        else:
            return GenericResponse(
                error_msg=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
    def delete(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.delete()
            return GenericResponse(
                        success_msg="Customer deleted Successfully",
                        status=status.HTTP_200_OK,
                    )
        else:
            return GenericResponse(
                error_msg=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
