from django.contrib import admin

from .models import EducationalProgram, Group, UserEducationalProgram


class EducationalProgramInline(admin.TabularInline):
    model = EducationalProgram
    extra = 0

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [EducationalProgramInline]
    list_display = (
        "title",
    )


@admin.register(UserEducationalProgram)
class UserEducationalProgramAdmin(admin.ModelAdmin):
    list_display = (
        "educational_program",
        "user",
    )
