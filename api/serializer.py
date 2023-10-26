from rest_framework import serializers
from django.contrib.auth import authenticate

from accounts.models import CustomUser

# User login serializer (Read-only): Validate user login credentials and perform user login
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect credenetials!")
        
# User registration serializer(Write): User registration is performed
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'password')
        extra_kwargs = {'password': {'write_only' : True}}          # password field is made write-only to protect sensitive information
    
    # Override default create method. Creates a new CustomUser instance with the email, password provided. 
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user
    