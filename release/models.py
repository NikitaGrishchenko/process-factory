
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

User = get_user_model()





class Release(models.Model):
    """
    Тематический выпуск
    """

    title = models.CharField(max_length=255, verbose_name=_("Название"))
    description = RichTextField(verbose_name=_("Описание"))
    date_of_event = models.DateField(_("Дата проведения"), auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = _("Тематический выпуск")
        verbose_name_plural = _("Тематический выпуск")

    def __str__(self):
        return self.title


class Document(models.Model):
    """
    Документ
    """

    title = models.CharField(max_length=255, verbose_name=_("Название"))
    file = models.FileField(_("Документ"), upload_to='release/', max_length=100)
    release = models.ForeignKey(
        Release,
        related_name='documents',
        verbose_name=_("Тематический выпуск"),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("Документ")
        verbose_name_plural = _("Документ")

    def __str__(self):
        return self.title
