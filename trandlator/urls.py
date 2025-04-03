from django.contrib import admin
from django.urls import path, include
from user.views import (UserCreateView, 
                                      UserSendMail, 
                                      UserVerifyEmail, 
                                      ResetPassword, 
                                      ChangePassword,
                                      UserTickerUpdate,
                                      UserDetailView)
from ticker.views import TickerView, TickerDetailView
from article.views import ArticleView
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

    path('user/', include('user.urls')),
    path('ticker/', include('ticker.urls')),
    path('article/', include('article.urls')),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
