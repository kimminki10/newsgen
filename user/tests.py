from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
import json

User = get_user_model()

class UserTest(TestCase):
    def setUp(self):
        """테스트 실행 전 초기화 작업"""
        self.client = Client()
        self.user_data = {
            'email': 'test@example.com',
            'password': 'testpassword123',
            'mail_frequency': 'everyday',
            'mail_timeSlot': 'onceDay',
            'mail_newsCount': 'oneNews'
        }
        self.url = reverse('user-create')
    
    def test_user_model_create(self):
        """User 모델 생성 테스트"""
        user = User.objects.create_user(
            email=self.user_data['email'],
            password=self.user_data['password']
        )
        
        self.assertEqual(user.email, self.user_data['email'])
        self.assertTrue(user.check_password(self.user_data['password']))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_email_verified)
        self.assertEqual(user.mail_frequency, 'everyday')
        self.assertEqual(user.mail_timeSlot, 'onceDay')
        self.assertEqual(user.mail_newsCount, 'oneNews')
    
    def test_user_create_view(self):
        """User 생성 API 엔드포인트 테스트"""
        response = self.client.post(
            self.url,
            data=json.dumps(self.user_data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.get(email=self.user_data['email'])
        self.assertEqual(user.email, self.user_data['email'])
        self.assertTrue(user.check_password(self.user_data['password']))
    
    def test_create_user_with_existing_email(self):
        """이미 존재하는 이메일로 유저 생성 시도 테스트"""
        # 먼저 유저 생성
        User.objects.create_user(
            email=self.user_data['email'],
            password=self.user_data['password']
        )
        
        # 같은 이메일로 다시 생성 시도
        response = self.client.post(
            self.url,
            data=json.dumps(self.user_data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
    
    def test_create_user_with_invalid_data(self):
        """유효하지 않은 데이터로 유저 생성 테스트"""
        invalid_data = self.user_data.copy()
        invalid_data['email'] = 'invalid-email'  # 유효하지 않은 이메일 형식
        
        response = self.client.post(
            self.url,
            data=json.dumps(invalid_data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)