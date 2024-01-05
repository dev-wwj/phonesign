from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import UserProfileSerializer

# Create your views here.

User = get_user_model()


class PhoneLoginView(APIView):

    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        verification_code = request.data.get('verification_code')

        user, created = CustomUser.objects.get_or_create(phone_number=phone_number)
        token, created = Token.objects.get_or_create(user=user)

        # Your logic to send and verify the verification code
        # Implement the code sending and verification logic here

        return Response({'message': 'Login successful',
                         'token': token.key, },
                        status=status.HTTP_200_OK)


class UserProfileView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)