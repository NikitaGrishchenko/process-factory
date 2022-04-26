from ckeditor.fields import RichTextField
from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import Group, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class ProxyGroup(Group):
    class Meta:
        proxy = True
        verbose_name = _("Группа")
        verbose_name_plural = _("Группы")


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, "
            "digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("Имя"), max_length=30)
    last_name = models.CharField(_("Фамилия"), max_length=150)
    patronymic = models.CharField(_("Отчество"), max_length=150)
    email = models.EmailField(_("Электронная почта"), unique=True)
    phone = models.CharField(_("Номер телефона"), max_length=25)
    is_staff = models.BooleanField(
        _("Администратор"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."
        ),
    )
    is_active = models.BooleanField(
        _("Активный"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("Дата создания учетной записи"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)



class Employee(models.Model):
    """
    Сотрудники
    """
    first_name = models.CharField(_("Имя"), max_length=30)
    last_name = models.CharField(_("Фамилия"), max_length=150)
    patronymic = models.CharField(_("Отчество"), max_length=150)
    position = models.CharField(_("Должность"), max_length=150)
    desc = RichTextField(verbose_name=_("Описание"))
    image = models.ImageField(null=True, blank=False, verbose_name=_("Фото"))

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


    def __str__(self):
        return f"{self.last_name}"

    def get_full_name(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"
