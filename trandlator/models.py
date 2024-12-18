from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100, default='empty title')
    content = models.TextField(default='empty content')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    origin_url = models.URLField(max_length=200, blank=True)
    tts_content = models.TextField(default='empty tts content')
    tts_url = models.URLField(max_length=200, blank=True)


class Ticker(models.Model):
    ticker_name = models.CharField(max_length=100, unique=True)
    articles = models.ManyToManyField(Article, related_name='tickers',blank=True)

    def __str__(self):
        return self.ticker_name


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    tickers = models.ManyToManyField(Ticker, related_name='users', blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser
    
    def has_module_perms(self, app_label):
        return self.is_superuser
