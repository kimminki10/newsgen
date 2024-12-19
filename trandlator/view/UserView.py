from rest_framework import generics
from trandlator.models import User
from trandlator.controller.UserSerialize import UserSerializer
from django.core.cache import cache
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
import uuid


def send_verification_email(t, email, url):
    token = str(uuid.uuid4())
    cache.set(token, {'type':t, 'value':email}, timeout=300)  # 5 minutes

    verification_link = url + token
    send_mail(
        'Verify your email',
        f'Click the link to verify your email: {verification_link}',
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(email=request.data['email'])
        send_verification_email('email', user.email, "http://localhost:5173/user/verify_email/")
        return response
    

class UserTickers(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.get(email=self.request.user.email).tickers.all()
    

class ResetPassword(generics.GenericAPIView):
    def post(self, request):
        email = request.data['email']
        user = User.objects.get(email=email)
        send_verification_email('password', user.email, "http://localhost:5173/reset-password/")
        return Response({'message': 'Password reset email sent'}, status=status.HTTP_200_OK)


class UserVerifyEmail(generics.GenericAPIView):
    def get(self, request, token):
        token_value = cache.get(token)
        if token_value is None or token_value['type'] != 'email':
            return Response({'error': 'Token expired'}, status=status.HTTP_400_BAD_REQUEST)
        email = token_value['value']
        user = User.objects.get(email=email)
        user.is_email_verified = True
        user.save()
        return Response({'message': 'Email verified'}, status=status.HTTP_200_OK)

class ChangePassword(generics.GenericAPIView):
    def post(self, request, token):
        token_value = cache.get(token)
        if token_value is None or token_value['type'] != 'password':
            return Response({'error': 'Token expired'}, status=status.HTTP_400_BAD_REQUEST)
        email = token_value['value']
        user = User.objects.get(email=email)
        user.set_password(request.data['password'])
        user.save()
        return Response({'message': 'Password changed'}, status=status.HTTP_200_OK)