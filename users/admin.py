from django.contrib import admin
from users.models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ("email", "first_name", "user_name")
    list_filter = ("email", "first_name", "user_name", "is_staff", "is_active")
    ordering = ("-start_date",)
    list_display = ("email", "first_name", "user_name", "is_staff", "is_active")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "first_name",
                    "user_name",
                ),
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
        ("Personal", {"fields": ("about",)}),
    )
    formfield_overrides = {
        models.TextField: {"widget": Textarea(attrs={"rows": 20, "cols": 60})}
    }
    add_fieldsets = (
        None,
        {
            "classes": ("wide",),
            "fields": (
                "email",
                "user_name",
                "first_name",
                "password1",
                "password2",
                "is_active",
            ),
        },
    )


admin.site.register(NewUser, UserAdminConfig)
