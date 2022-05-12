from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from .models import QuestionsFromGuests

User = get_user_model()


class UserRegistrationForm(forms.ModelForm):
    """
    Форма регистрации пользователей
    """

    consent = forms.BooleanField(
        label=_("Согласие на обработку персональных данных")
    )
    password = forms.CharField(
        label=_("Введите пароль"), widget=forms.PasswordInput()
    )
    confirm_password = forms.CharField(
        label=_("Повторите пароль"), widget=forms.PasswordInput()
    )
    email = forms.EmailField(label=_("E-mail"))

    def clean_confirm_password(self):
        valid = (
            self.cleaned_data["password"]
            == self.cleaned_data["confirm_password"]
        )
        if len(self.cleaned_data["password"]) < 8:
            raise forms.ValidationError(
                "Пароль должен содержать минимум 8 символов"
            )
        if not valid:
            raise forms.ValidationError("Пароли не совпадают")
        return self.cleaned_data["confirm_password"]

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "patronymic",
            "phone",
            "email",
        )


class QuestionsFromGuestsForm(forms.ModelForm):
    """
    Форма обратной связи
    """

    consent = forms.BooleanField(
        label=_("Согласие на обработку персональных данных")
    )
    email = forms.EmailField(label=_("E-mail"))


    class Meta:
        model = QuestionsFromGuests
        fields = (
            "first_name",
            "last_name",
            "patronymic",
            "phone",
            "email",
            "phone",
            "text",
        )
