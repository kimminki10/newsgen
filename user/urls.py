from django.urls import path
from .views import UserCreateView, UserSendMail, UserVerifyEmail, ResetPassword, ChangePassword, UserTickerUpdate, UserDetailView

urlpatterns = [
    path('', UserCreateView.as_view(), name='user-create'),
    path('update/', UserTickerUpdate.as_view(), name='user_tickers_update'),
    path('verify_email/<str:token>/', UserVerifyEmail.as_view(), name='verify_email'),
    path('resend_verification/', UserCreateView.as_view(), name='resend_verification'),
    path('reset_password/', ResetPassword.as_view(), name='reset_password'),
    path('change_password/<str:token>/', ChangePassword.as_view(), name='change_password'),
    path('<str:email>/', UserDetailView.as_view(), name='user_detail'),
    path('mail/send/', UserSendMail.as_view(), name='user_send_mail'),
]