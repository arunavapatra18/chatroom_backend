from rest_framework.serializers import ModelSerializer

from accounts.models import CustomUser

class CustomUserSerializer(ModelSerializer):
    class Meta:
        pass