from django.contrib import admin
from django.utils.html import format_html
from .models import Application, Programme, Faculty


@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("unique_code", "full_name", "programme",
                    "faculty", "phone_number", "colored_status", "created_at")
    list_filter = ("status", "programme", "faculty", "created_at")
    search_fields = ("unique_code", "first_name", "last_name",
                     "middle_name", "passport_number", "phone_number", "email")
    readonly_fields = ("unique_code", "created_at", "updated_at",
                       "photo_preview")
    list_per_page = 25
    date_hierarchy = "created_at"
    autocomplete_fields = ("programme", "faculty")
    fieldsets = (
        ("Ariza kodi va holati", {
            "fields": ("unique_code", "status", "admin_note")}),
        ("Yo'nalish", {"fields": ("programme", "faculty")}),
        ("Shaxsiy ma'lumotlar", {
            "fields": ("last_name", "first_name", "middle_name",
                       "date_of_birth", "passport_number")}),
        ("Aloqa", {"fields": ("phone_number", "email")}),
        ("Hujjatlar", {
            "fields": ("passport_file", "diploma_transcript",
                       "school_certificate", "photo", "photo_preview",
                       "certificate")}),
        ("Tizim", {"fields": ("user", "created_at", "updated_at")}),
    )

    @admin.display(description="Holati")
    def colored_status(self, obj):
        colors = {"kutilmoqda": "#e0a800",
                  "qabul_qilindi": "#28a745", "rad_etildi": "#dc3545"}
        return format_html(
            '<b style="color:{}">{}</b>',
            colors.get(obj.status, "#666"), obj.get_status_display())

    @admin.display(description="Foto")
    def photo_preview(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" style="max-height:150px;border-radius:6px"/>',
                obj.photo.url)
        return "—"
