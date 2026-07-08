"""Pluggable SMS service.

Phone verification is currently DISABLED (registration needs no code).
This module is kept so we can switch OTP on later by setting
SMS_BACKEND=console|eskiz and PHONE_VERIFICATION_REQUIRED=True — no other
code needs to change.
"""
import logging
from django.conf import settings

logger = logging.getLogger(__name__)


def send_sms(phone_number: str, message: str) -> bool:
    backend = getattr(settings, "SMS_BACKEND", "off")

    if backend == "off":
        return True

    if backend == "console":
        logger.info("[SMS -> %s] %s", phone_number, message)
        print(f"[SMS -> {phone_number}] {message}")
        return True

    if backend == "eskiz":
        return _send_eskiz(phone_number, message)

    logger.warning("Noma'lum SMS_BACKEND: %s", backend)
    return False


def _send_eskiz(phone_number: str, message: str) -> bool:
    import requests
    base = "https://notify.eskiz.uz/api"
    try:
        auth = requests.post(f"{base}/auth/login", data={
            "email": settings.ESKIZ_EMAIL,
            "password": settings.ESKIZ_PASSWORD,
        }, timeout=15)
        token = auth.json()["data"]["token"]
        resp = requests.post(
            f"{base}/message/sms/send",
            headers={"Authorization": f"Bearer {token}"},
            data={
                "mobile_phone": phone_number.lstrip("+"),
                "message": message,
                "from": "4546",
            },
            timeout=15,
        )
        return resp.status_code in (200, 201)
    except Exception as exc:  # noqa: BLE001
        logger.error("Eskiz SMS xatosi: %s", exc)
        return False
