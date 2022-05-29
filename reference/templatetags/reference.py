from django import template

from ..models import News

# from django.db.models import Q


register = template.Library()


@register.inclusion_tag("components/last-news.html")
def last_news() -> dict:
    return {
        "news": News.objects.all().order_by("-id")[:6],
    }
