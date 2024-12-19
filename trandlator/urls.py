from django.contrib import admin
from django.urls import path
from trandlator.view.UserView import (UserCreateView, 
                                      UserTickers, 
                                      UserVerifyEmail, 
                                      ResetPassword, 
                                      ChangePassword,
                                      UserTickerUpdate)
from trandlator.view.TickerView import TickerView, TickerDetailView
from trandlator.view.ArticleView import ArticleView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    #path('', test, name='home'),  # 루트 경로 ("/")
    path('admin/', admin.site.urls),  # Django 관리자 페이지
    path('user/', UserCreateView.as_view(), name='user'),
    path('user/tickers/', UserTickers.as_view(), name='user_tickers'),
    path('user/tickers/update/', UserTickerUpdate.as_view(), name='user_tickers_update'),
    path('user/verify_email/<str:token>/', UserVerifyEmail.as_view(), name='verify_email'),
    path('user/resend_verification/', UserCreateView.as_view(), name='resend_verification'),
    path('user/reset_password/', ResetPassword.as_view(), name='reset_password'),
    path('user/change_password/<str:token>/', ChangePassword.as_view(), name='change_password'),
    path('ticker/', TickerView.as_view(), name='ticker'),
    path('ticker/<str:ticker_name>/', TickerDetailView.as_view(), name='ticker_detail'),
    path('article/', ArticleView.as_view(), name='article'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
