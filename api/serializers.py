from rest_framework import serializers
from .models import registration

class RegistrationSerializer(serializers.ModelSerializer):
 class Meta:
  model = registration
  fields = '__all__'