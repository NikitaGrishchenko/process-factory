from django import template

from ..models import BusinessGames

register = template.Library()


@register.inclusion_tag("components/last-business.html")
def last_business() -> dict:
    business = BusinessGames.objects.all().order_by('-id')[:6]
    return {
        "business": business,
    }
