from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .models import FeedbackUserBusinessGames

User = get_user_model()

class FeedbackUserBusinessGamesForm(forms.ModelForm):
    """
    Форма отправки отзыва
    """

    class Meta:
        model = FeedbackUserBusinessGames
        fields = ("text",)
