from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group as BaseGroup

from .models import (Certificate, Employee, ProxyGroup, QuestionsFromGuests,
                     User)


class CertificateInline(admin.TabularInline):
    model = Certificate
    extra = 0

@admin.register(User)
class UserAdmin(BaseUserAdmin):

    inlines = [CertificateInline]
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "patronymic",
        "phone",
    )
    list_readonly_not_superuser_fields = (
        "is_superuser",
        "is_staff",
        "last_login",
        "date_joined",
    )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            ("Персональная информация"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "patronymic",
                    "email",
                    "phone",
                )
            },
        ),
        (
            ("Права"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Активность"), {"fields": ("last_login", "date_joined")}),
    )

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "patronymic",
        "position",
        "desc",
        "image",
    )

@admin.register(QuestionsFromGuests)
class QuestionsFromGuestsAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "patronymic",
        "email",
        "phone",
        "text",
        "date_created",
    )


admin.site.unregister(BaseGroup)
admin.site.register(ProxyGroup, GroupAdmin)
