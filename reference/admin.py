from django.contrib import admin

from .models import Site, QualityLibrary


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = (
        "title",
    )

@admin.register(QualityLibrary)
class QualityLibraryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
    )
