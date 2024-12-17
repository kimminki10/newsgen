from rest_framework import generics
from trandlator.model.UserModel import User
from trandlator.controller.UserSerialize import UserSerializer
from django.core.cache import cache
from django.core.mail import send_mail
from django.conf import settings
import uuid


def send_verification_email(request, email):
    # Generate token
    token = str(uuid.uuid4())
    cache.set(token, email, timeout=300)  # 5 minutes

    # Send email
    verification_link = "http://verificationlink"
    send_mail(
        'Verify your email',
        f'Click the link to verify your email: {verification_link}',
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=request.data['username'])
        send_verification_email(request, user.email)
        return response
    

class UserTickers(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.get(username=self.request.user.username).tickers.all()