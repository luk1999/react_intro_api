from django.contrib import admin

from games.models import Comment, Developer, Game, Genre, Platform, Rating


class CommentAdmin(admin.ModelAdmin):
    list_display = ("game", "created_by", "created_at")
    exclude = ("created_by",)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)


class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "developer", "genre", "platform", "rating", "released_at")
    prepopulated_fields = {"slug": ("title",)}

    def get_changeform_initial_data(self, request):
        return {
            "meta_score": 0,
            "user_score": 0,
        }


admin.site.register(Comment, CommentAdmin)
admin.site.register(Developer)
admin.site.register(Game, GameAdmin)
admin.site.register(Genre)
admin.site.register(Platform)
admin.site.register(Rating)
