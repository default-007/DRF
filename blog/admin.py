from django.contrib import admin
from . import models


@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("title", "id", "status", "slug", "author")
    prepopulated_fields = {
        "slug": ("title", "author"),
    }


admin.site.register(models.Category)

# Register your models here.
