from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    '''Менеджер для управления пользователями, в котором реализуется логика их создания.'''

    def create_user(self, username, email, password=None):
        '''Для создания обычных пользователей.'''

        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        # Для нормализации адреса электронной почты.
        email = self.normalize_email(email) # например, приведение к нижнему регистру.
        # Автоматическая ссылка на модель, связанную с этим менеджером.
        user = self.model(username=username, email=email)
        # Хэширует пароль перед его сохранением.
        user.set_password(password)
        # Для сохранения объекта в БД.
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        '''Для создания суперпользователей с дополнительными правами.'''

        user = self.create_user(username, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    '''Пользовательская модель пользователя.'''

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    # Указывает поле которое будет использоваться для аутентификации.
    USERNAME_FIELD = 'email'
    # Дополнительные обязательные поля при создании суперпользователя.
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
