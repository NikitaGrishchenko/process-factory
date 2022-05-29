from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .models import FeedbackToEducationalProgram

User = get_user_model()

class FeedbackToEducationalProgramForm(forms.ModelForm):
    """
    Форма отправки отзыва
    """

    class Meta:
        model = FeedbackToEducationalProgram
        fields = ("text",)
