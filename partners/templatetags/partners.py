from django import template

from ..models import Аrea

# from django.db.models import Q


register = template.Library()


@register.inclusion_tag("components/partners.html")
def partners() -> dict:
    area = Аrea.objects.order_by('order')
    return {
        "area": area,
    }
