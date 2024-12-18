from django.contrib import admin
from django.urls import path
from trandlator.view.UserView import UserListCreate, UserTickers
from trandlator.view.TickerView import TickerView
from trandlator.view.ArticleView import ArticleView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    #path('', test, name='home'),  # 루트 경로 ("/")
    path('admin/', admin.site.urls),  # Django 관리자 페이지
    path('user/', UserListCreate.as_view(), name='user'),
    path('user/tickers/', UserTickers.as_view(), name='user_tickers'),
    path('ticker/', TickerView.as_view(), name='ticker'),
    path('article/', ArticleView.as_view(), name='article'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
