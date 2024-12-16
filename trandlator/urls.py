from django.contrib import admin
from django.urls import path
from trandlator.view.UserView import TestAPIView



urlpatterns = [
    #path('', test, name='home'),  # 루트 경로 ("/")
    path('admin/', admin.site.urls),  # Django 관리자 페이지
    path('test/', TestAPIView.as_view(), name='test'),
]
