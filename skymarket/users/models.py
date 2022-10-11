from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles:
    USER = "Пользователь"
    ADMIN = "Администратор"
    ROLES = [
        (USER, "Пользователь"),
        (ADMIN, "Администратор"),
    ]


class User(AbstractBaseUser):
    email = models.EmailField(
        unique=True,
        max_length=100,
        help_text="Укажите электронную почту"
    )

    first_name = models.CharField(
        max_length=200,
        verbose_name="Имя",
        help_text="Введите имя"
        )

    last_name = models.CharField(
        max_length=200,
        verbose_name="Фамилия",
        help_text="Введите фамилию"
        )

    phone = PhoneNumberField(
        verbose_name="Телефон для связи",
        help_text="Укажите телефон для связи"
    )

    role = models.CharField(
        max_length=13,
        choices=UserRoles.ROLES,
        default=UserRoles.USER,
        verbose_name="Роль пользователя",
        help_text="Укажите роль"
    )

    is_active = models.BooleanField(
        verbose_name="Аккаунт активен"
    )

    # эта константа определяет поле для логина пользователя
    USERNAME_FIELD = "email"

    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ["first_name", "last_name", "phone", "role"]

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER
