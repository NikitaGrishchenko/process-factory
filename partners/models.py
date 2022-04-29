
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

User = get_user_model()



class Аrea(models.Model):
    """
    Область дейстельности
    """

    title = models.CharField(max_length=255, verbose_name=_("Название"))
    color = ColorField(verbose_name=_("Цвет панели"))
    order = models.IntegerField(_("Порядок вывода"))

    class Meta:
        verbose_name = _("Область дейстельности")
        verbose_name_plural = _("Область дейстельности")

    def __str__(self):
        return self.title

class Partner(models.Model):
    """
    Партнер
    """

    title = models.CharField(max_length=255, verbose_name=_("Название"))
    area = models.ForeignKey(
        Аrea,
        verbose_name=_("Область дейстельности"),
        on_delete=models.CASCADE,
        related_name="partner",
    )
    image = models.ImageField(verbose_name=_("Картинка"))
    order = models.IntegerField(_("Порядок вывода"))

    class Meta:
        verbose_name = _("Партнер")
        verbose_name_plural = _("Партнеры")

    def __str__(self):
        return self.title
