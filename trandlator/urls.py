from django.contrib import admin
from django.urls import path
from user.views import (UserCreateView, 
                                      UserSendMail, 
                                      UserVerifyEmail, 
                                      ResetPassword, 
                                      ChangePassword,
                                      UserTickerUpdate,
                                      UserDetailView)
from trandlator.view.TickerView import TickerView, TickerDetailView
from trandlator.view.ArticleView import ArticleView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="NewsGen API",
        default_version='v1',
        description="NewsGen API 문서",
        contact=openapi.Contact(email="pangshe10@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    #path('', test, name='home'),  # 루트 경로 ("/")
    path('admin/', admin.site.urls),  # Django 관리자 페이지
    path('user/', UserCreateView.as_view(), name='user-create'),
    path('user/update/', UserTickerUpdate.as_view(), name='user_tickers_update'),
    path('user/verify_email/<str:token>/', UserVerifyEmail.as_view(), name='verify_email'),
    path('user/resend_verification/', UserCreateView.as_view(), name='resend_verification'),
    path('user/reset_password/', ResetPassword.as_view(), name='reset_password'),
    path('user/change_password/<str:token>/', ChangePassword.as_view(), name='change_password'),
    path('user/<str:email>/', UserDetailView.as_view(), name='user_detail'),
    path('user/mail/send/', UserSendMail.as_view(), name='user_send_mail'),
    path('ticker/', TickerView.as_view(), name='ticker'),
    path('ticker/<str:ticker_name>/', TickerDetailView.as_view(), name='ticker_detail'),
    path('article/', ArticleView.as_view(), name='article'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
