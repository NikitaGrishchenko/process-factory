
from datetime import datetime

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


class OurProjects(models.Model):
    """
    Наши проекты
    """

    title = models.CharField(max_length=255, verbose_name=_("Название"))
    description = RichTextField(verbose_name=_("Описание"))
    image_before = models.ImageField(verbose_name=_("Картинка до"))
    image_after = models.ImageField(verbose_name=_("Картинка после"))
    date_of_the_event = models.DateTimeField(_("Дата проведения"))



    class Meta:
        verbose_name = _("Наши проекты")
        verbose_name_plural = _("Наши проекты")

    def __str__(self):
        return self.title


class Document(models.Model):
    """
    Документ
    """

    title = models.CharField(max_length=255, verbose_name=_("Название"))
    file = models.FileField(_("Документ"), upload_to='our_projects/', max_length=100)
    our_projects = models.ForeignKey(
        OurProjects,
        related_name='documents',
        verbose_name=_("Проект"),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("Документ")
        verbose_name_plural = _("Документ")

    def __str__(self):
        return self.title



class News(models.Model):
    """
    Новости
    """

    title = models.CharField(max_length=255, verbose_name=_("Анонс"))
    image = models.ImageField(null=False, blank=False, verbose_name=_("Фото"))
    text = RichTextField(verbose_name=_("Текст"))
    date = models.DateTimeField(
        default=datetime.now, verbose_name=_("Дата публикации")
    )

    class Meta:
        verbose_name = _("Новость")
        verbose_name_plural = _("Новости")

    def __str__(self):
        return self.title

