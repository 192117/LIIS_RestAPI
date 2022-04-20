from django.conf import settings
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class MyUserManager(BaseUserManager):
    def _create_user(self, email, password, role, **extra_fields):
        if not email:
            raise ValueError("Вы не ввели Email")
        user = self.model(
            email=self.normalize_email(email),
            role=role,
            **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, role, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, role, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email', unique=True)
    role = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'

    objects = MyUserManager()


class Article(models.Model):
    body = models.TextField()
    public = models.BooleanField(default=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='email')
