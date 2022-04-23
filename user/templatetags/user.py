from django import template

from ..models import Employee

# from django.db.models import Q


register = template.Library()


@register.inclusion_tag("components/employee-list.html")
def employee() -> dict:
    employees = Employee.objects.all()
    return {
        "employees": employees,
    }

# @register.inclusion_tag("components/basic-information-last-news.html")
# def basic_information_last_news() -> dict:
#     latest_five_advertising = Advertising.objects.all().order_by("-id")[:5]
#     latest_five_news = News.objects.all().order_by("-id")[:5]

#     return {
#         "ads": latest_five_advertising,
#         "news": latest_five_news,
#     }
