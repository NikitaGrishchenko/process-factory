from django.apps import AppConfig


class ProgramConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'program'
    verbose_name = "Образовательные программы"
    verbose_name_plural = "Образовательные программы"
