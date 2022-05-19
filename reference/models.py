
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Site(models.Model):
    """
    Сайты
    """

    title = models.CharField(max_length=255, verbose_name=_("Наименование"))
    url = models.URLField(_("Ссылка"), max_length=200)

    class Meta:
        verbose_name = _("Сайты")
        verbose_name_plural = _("Сайты")

    def __str__(self):
        return self.title


class QualityLibrary(models.Model):
    """
    Библиотека качества
    """
    CHOICES = (
        ('book', 'Книжный вариант'),
        ('elec', 'Электронный вариант')
    )

    title = models.CharField(max_length=255, verbose_name=_("Наименование"))
    url = models.URLField(_("Ссылка"), max_length=200)
    type = models.CharField(_("Тип"), max_length=50, choices = CHOICES)

    class Meta:
        verbose_name = _("Библиотека качества")
        verbose_name_plural = _("Библиотека качества")

    def __str__(self):
        return self.title
