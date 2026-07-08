from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "display_name", "phone_number",
                    "email", "is_staff", "is_active", "date_joined")
    list_filter = ("is_staff", "is_active", "is_superuser")
    search_fields = ("username", "first_name", "last_name",
                     "phone_number", "email")
    ordering = ("-date_joined",)
    fieldsets = UserAdmin.fieldsets + (
        ("Qo'shimcha", {"fields": ("phone_number", "photo",
                                   "is_phone_verified")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Qo'shimcha", {"fields": ("phone_number",)}),
    )
