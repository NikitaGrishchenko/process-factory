from django.contrib import admin

from .models import Document, Release


class DocumentInline(admin.TabularInline):
    model = Document
    extra = 0

@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    inlines = [DocumentInline]
    list_display = (
        "title",
    )
