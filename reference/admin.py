from django.contrib import admin

from .models import Document, OurProjects, QualityLibrary, Site


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


class DocumentInline(admin.TabularInline):
    model = Document
    extra = 0

@admin.register(OurProjects)
class OurProjectsAdmin(admin.ModelAdmin):
    inlines = [DocumentInline]
    list_display = (
        "title",
    )
