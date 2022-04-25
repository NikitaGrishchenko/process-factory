from django import template

from ..models import EducationalProgram

# from django.db.models import Q


register = template.Library()


@register.inclusion_tag("components/last-programs.html")
def last_programs() -> dict:
    programs = EducationalProgram.objects.all()[:6]
    return {
        "programs": programs,
    }
