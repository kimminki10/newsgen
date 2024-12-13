from django.contrib import admin
from django.urls import path
from trandlator.UserModel import test

urlpatterns = [
    #path('', test, name='home'),  # 루트 경로 ("/")
    path('admin/', admin.site.urls),  # Django 관리자 페이지
    path('test/', test, name='test'),  # /test/ 경로
]
