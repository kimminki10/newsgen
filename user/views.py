from rest_framework import generics
from trandlator.models import Ticker
from user.models import User
from .serializer import UserSerializer
from trandlator.controller.TickerSerialize import TickerSerializer
from trandlator.controller.TickerSerialize import TickerNameSerializer
from django.core.cache import cache
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
import uuid


def send_verification_email(t, email, url):
    token = str(uuid.uuid4())
    cache.set(token, {'type':t, 'value':email}, timeout=300)  # 5 minutes

    verification_link = url + token
    send_mail(
        'Verify your email',
        f'Click the link to verify your email: {verification_link}',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(
        operation_description="Create a new user",
        responses={201: UserSerializer}
    )

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(email=request.data['email'])
        send_verification_email('email', user.email, f"http://{settings.HOST_NAME}/verify-email/")
        return response
    
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'email'
    

class UserTickers(generics.ListAPIView):
    serializer_class = TickerNameSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.get(email=self.request.user.email).tickers.all()
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = TickerNameSerializer(queryset, many=True)
        return Response(serializer.data)
    
class UserSendMail(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = User.objects.get(email=request.user.email)
        tickers = user.tickers.all()
        for ticker in tickers:
            articles = ticker.articles.all()
            for article in articles:
                send_mail(
                    'News',
                    f'{article.title}\n{article.content}',
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=False,
                )
        return Response({'message': 'Mail sent'}, status=status.HTTP_200_OK)
    
class UserTickerUpdate(generics.UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.get(email=self.request.user.email)
    
    def update(self, request, *args, **kwargs):
        user = self.get_queryset()
        tickers = Ticker.objects.filter(ticker_name__in=request.data['tickers']).all()
        user.tickers.set(tickers)
        user.mail_frequency = request.data['mail_frequency']
        user.mail_timeSlot = request.data['mail_timeSlot']
        user.mail_newsCount = request.data['mail_newsCount']
        user.save()
        return Response({'message': 'Tickers updated'}, status=status.HTTP_200_OK)
    

class ResetPassword(generics.GenericAPIView):
    def post(self, request):
        email = request.data['email']
        user = User.objects.get(email=email)
        send_verification_email('password', user.email, f"http://{settings.HOST_NAME}/reset-password/")
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
        cache.delete(token)
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