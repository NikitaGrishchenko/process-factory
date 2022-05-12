
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

User = get_user_model()



class Group(models.Model):
    """
    Группа
    """

    title = models.CharField(max_length=255, verbose_name=_("Название"))

    class Meta:
        verbose_name = _("Группа")
        verbose_name_plural = _("Группы")

    def __str__(self):
        return self.title

class BusinessGames(models.Model):
    """
    Деловые игры
    """

    title = models.CharField(max_length=255, verbose_name=_("Название"))
    group = models.ForeignKey(
        Group,
        verbose_name=_("Группа"),
        on_delete=models.CASCADE,
    )
    description = RichTextField(verbose_name=_("Описание"))



    class Meta:
        verbose_name = _("Деловая игра")
        verbose_name_plural = _("Деловые игры")



    def __str__(self):
        return self.title



class UserBusinessGames(models.Model):
    """
    Участие пользователя в деловой игры
    """


    business_games = models.ForeignKey(
        BusinessGames,
        verbose_name=_("Деловая игра"),
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Пользователь"))
    date_joined = models.DateTimeField(_("Дата создания учетной записи"), default=timezone.now)

    class Meta:
        verbose_name = _("Участник")
        verbose_name_plural = _("Участник")

    def __str__(self):
        return f"{self.user} {self.business_games}"
