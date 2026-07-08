import secrets
import string
from django.conf import settings
from django.db import models
from django.utils import timezone


def generate_unique_code():
    """Human-readable, collision-checked code, e.g. NUB-2026-7F3K9Q."""
    alphabet = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"  # no confusing 0/O/1/I
    year = timezone.now().year
    while True:
        suffix = "".join(secrets.choice(alphabet) for _ in range(6))
        code = f"NUB-{year}-{suffix}"
        if not Application.objects.filter(unique_code=code).exists():
            return code


class Programme(models.Model):
    name = models.CharField("Nomi", max_length=200, unique=True)
    is_active = models.BooleanField("Faol", default=True)

    class Meta:
        verbose_name = "Yo'nalish (dastur)"
        verbose_name_plural = "Yo'nalishlar (dasturlar)"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField("Nomi", max_length=200, unique=True)
    is_active = models.BooleanField("Faol", default=True)

    class Meta:
        verbose_name = "Fakultet"
        verbose_name_plural = "Fakultetlar"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Application(models.Model):
    class Status(models.TextChoices):
        PENDING = "kutilmoqda", "Kutilmoqda"
        ACCEPTED = "qabul_qilindi", "Qabul qilindi"
        REJECTED = "rad_etildi", "Rad etildi"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="application",
        verbose_name="Foydalanuvchi",
    )
    programme = models.ForeignKey(
        Programme, on_delete=models.PROTECT,
        verbose_name="Yo'nalish", related_name="applications",
    )
    faculty = models.ForeignKey(
        Faculty, on_delete=models.PROTECT,
        verbose_name="Fakultet", related_name="applications",
    )

    first_name = models.CharField("Ism", max_length=100)
    last_name = models.CharField("Familiya", max_length=100)
    middle_name = models.CharField("Otasining ismi", max_length=100, blank=True)
    date_of_birth = models.DateField("Tug'ilgan sana")
    passport_number = models.CharField("Passport raqami", max_length=20)
    phone_number = models.CharField("Telefon raqami", max_length=20)
    email = models.EmailField("Email")

    passport_file = models.FileField(
        "Passport", upload_to="documents/passport/")
    diploma_transcript = models.FileField(
        "Diplom ilovasi (magistratura uchun)",
        upload_to="documents/transcript/", blank=True, null=True)
    school_certificate = models.FileField(
        "Attestat yoki diplom nusxasi", upload_to="documents/certificate/")
    photo = models.ImageField(
        "Foto (3x4)", upload_to="documents/photo/")
    certificate = models.FileField(
        "Sertifikat (mavjud bo'lsa)",
        upload_to="documents/extra_certificate/", blank=True, null=True)

    unique_code = models.CharField(
        "Ariza kodi", max_length=20, unique=True, editable=False, db_index=True)
    status = models.CharField(
        "Holati", max_length=20,
        choices=Status.choices, default=Status.PENDING)
    admin_note = models.TextField("Admin izohi", blank=True)

    created_at = models.DateTimeField("Yaratilgan", auto_now_add=True)
    updated_at = models.DateTimeField("Yangilangan", auto_now=True)

    class Meta:
        verbose_name = "Ariza"
        verbose_name_plural = "Arizalar"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.unique_code} — {self.last_name} {self.first_name}"

    def save(self, *args, **kwargs):
        if not self.unique_code:
            self.unique_code = generate_unique_code()
        super().save(*args, **kwargs)

    @property
    def full_name(self):
        parts = [self.last_name, self.first_name, self.middle_name]
        return " ".join(p for p in parts if p)

    @property
    def status_color(self):
        return {
            self.Status.PENDING: "warning",
            self.Status.ACCEPTED: "success",
            self.Status.REJECTED: "danger",
        }.get(self.status, "secondary")
