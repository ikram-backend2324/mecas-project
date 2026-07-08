from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()

DEFAULT_USERNAME = "admin"
DEFAULT_PASSWORD = "admin123"

STARTER_PROGRAMMES = [
    "Bakalavriat", "Magistratura",
]
STARTER_FACULTIES = [
    "Axborot texnologiyalari",
    "Energetika",
    "Qurilish",
    "Iqtisodiyot va menejment",
    "Mexanika",
]


class Command(BaseCommand):
    help = ("Creates default superuser (admin / admin123) and a few "
            "starter programmes/faculties if they are missing.")

    def handle(self, *args, **options):
        # Superuser
        if User.objects.filter(username=DEFAULT_USERNAME).exists():
            self.stdout.write(self.style.WARNING(
                f"'{DEFAULT_USERNAME}' allaqachon mavjud. O'tkazib yuborildi."))
        else:
            User.objects.create_superuser(
                username=DEFAULT_USERNAME,
                password=DEFAULT_PASSWORD,
                email="admin@example.com",
                is_phone_verified=True,
            )
            self.stdout.write(self.style.SUCCESS(
                f"Superuser yaratildi: {DEFAULT_USERNAME} / {DEFAULT_PASSWORD}"))

        # Starter choices (import here so migrations always run first)
        from applications.models import Programme, Faculty
        for name in STARTER_PROGRAMMES:
            Programme.objects.get_or_create(name=name)
        for name in STARTER_FACULTIES:
            Faculty.objects.get_or_create(name=name)
        self.stdout.write(self.style.SUCCESS(
            "Boshlang'ich yo'nalish va fakultetlar tayyor."))
