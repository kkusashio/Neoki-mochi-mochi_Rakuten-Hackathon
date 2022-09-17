from typing import Any, Optional

from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str, username: str) -> 'User':
        user = User(
            email=BaseUserManager.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)

        # トークンの作成
        Token.objects.create(user=user)
        return user

    def create_superuser(self, email: str, password: str, username: str) -> 'User':
        u = self.create_user(email=email, password=password, username=username)
        u.is_staff = True
        u.is_superuser = True
        u.save(using=self._db)
        return u


class User(AbstractBaseUser, PermissionsMixin):
    password = models.CharField(
        _('password'),
        max_length=128
        )
    username = models.CharField(
        blank=False,
        unique=True,
        max_length=150
        )
    email = models.EmailField(
        unique=True,
        blank=False
        )
    rate = models.IntegerField(
        # TODO デフォルト設定する？
        blank=True,
        default=1000,
        )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']

    objects = UserManager()
