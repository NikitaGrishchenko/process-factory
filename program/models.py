
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

class EducationalProgram(models.Model):
    """
    Образовательная программа
    """

    title = models.CharField(max_length=255, verbose_name=_("Название"))
    group = models.ForeignKey(
        Group,
        verbose_name=_("Группа"),
        on_delete=models.CASCADE,
    )
    description = RichTextField(verbose_name=_("Описание"))



    class Meta:
        verbose_name = _("Образовательная программа")
        verbose_name_plural = _("Образовательная программа")



    def __str__(self):
        return self.title



class UserEducationalProgram(models.Model):
    """
    Участие пользователя в программе
    """


    educational_program = models.ForeignKey(
        EducationalProgram,
        verbose_name=_("Образовательная программа"),
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Пользователь"))
    date_joined = models.DateTimeField(_("Дата создания учетной записи"), default=timezone.now)



    class Meta:
        verbose_name = _("Участник")
        verbose_name_plural = _("Участник")

    def __str__(self):
        return f"{self.user} {self.educational_program}"
