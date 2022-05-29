from django.contrib import admin

from .models import (BusinessGames, FeedbackUserBusinessGames, Group,
                     UserBusinessGames)


class BusinessGamesInline(admin.TabularInline):
    model = BusinessGames
    extra = 0

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [BusinessGamesInline]
    list_display = (
        "title",
    )


@admin.register(UserBusinessGames)
class UserBusinessGamesAdmin(admin.ModelAdmin):
    list_display = (
        "business_games",
        "user",
    )


@admin.register(FeedbackUserBusinessGames)
class FeedbackUserBusinessGamesAdmin(admin.ModelAdmin):
    pass
