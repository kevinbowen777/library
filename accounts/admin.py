from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = [
        "email",
        "username",
        "is_staff",
    ]
    """
    fieldsets = UserAdmin.fieldsets
    fieldsets[1][1]["fields"] = fieldsets[1][1]["fields"] + (
        "age",
        "country",
        "profile_pic",
        "bio",
    )
    """
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal information",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "age",
                    "country",
                    "profile_pic",
                    "bio",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )


# admin.site.register(User, CustomUserAdmin)
