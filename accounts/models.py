from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.CharField(
        "Telefon raqami", max_length=20, blank=True
    )
    photo = models.ImageField(
        "Rasm", upload_to="profile_photos/", blank=True, null=True
    )
    # Reserved for the future SMS flow. Defaults to True so that, for now,
    # registration works without any phone verification step.
    is_phone_verified = models.BooleanField("Telefon tasdiqlangan", default=True)

    def __str__(self):
        return self.get_full_name() or self.username

    @property
    def display_name(self):
        full = self.get_full_name()
        return full if full else self.username
