from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from .serializer import UserLoginSerializer, UserRegisterSerializer

# Create your views here.
class AuthLoginAPIView(APIView):
    
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data
        token, _ = Token.objects.get_or_create(user=user)
        
        return Response({'token':token.key}, status=status.HTTP_200_OK)
    
class AuthLogoutAPIView(APIView):
    # TODO
    pass
