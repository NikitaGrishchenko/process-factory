from django.contrib import admin

from .models import Partner, Аrea


class PartnerInline(admin.TabularInline):
    model = Partner
    extra = 0

@admin.register(Аrea)
class GroupAdmin(admin.ModelAdmin):
    inlines = [PartnerInline]
    list_display = (
        "title",
    )
