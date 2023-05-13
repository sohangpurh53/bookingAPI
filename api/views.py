from django.shortcuts import render
from .models import registration
from .serializers import RegistrationSerializer
from rest_framework import generics
# Create your views here.

class RegisterView(generics.ListCreateAPIView):
    queryset = registration.objects.all()
    serializer_class = RegistrationSerializer

class SingleRegisterView(generics.RetrieveUpdateDestroyAPIView):
    queryset = registration.objects.all()
    serializer_class = RegistrationSerializer