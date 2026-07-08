import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-dev-key-change-me-in-production-nubel-belarus-portal",
)

DEBUG = os.environ.get("DEBUG", "True").lower() == "true"

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")

CSRF_TRUSTED_ORIGINS = [
    o for o in os.environ.get(
        "CSRF_TRUSTED_ORIGINS",
        "https://*.onrender.com",
    ).split(",") if o
]

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "accounts",
    "applications",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "nubel_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "applications.context_processors.language",
            ],
        },
    },
]

WSGI_APPLICATION = "nubel_project.wsgi.application"

# --- Database ---------------------------------------------------------------
# Uses DATABASE_URL exactly as requested. For local dev we fall back to a
# sqlite URL so the project runs without a Postgres instance; production
# stays PostgreSQL with no code change.
if not os.environ.get("DATABASE_URL"):
    os.environ["DATABASE_URL"] = f"sqlite:///{BASE_DIR / 'db.sqlite3'}"

DATABASES = {
    "default": dj_database_url.parse(
        os.environ.get("DATABASE_URL")
    )
}

AUTH_USER_MODEL = "accounts.CustomUser"

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
     "OPTIONS": {"min_length": 6}},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --- Localization (Uzbekistan) ---------------------------------------------
LANGUAGE_CODE = "uz"
TIME_ZONE = "Asia/Tashkent"
USE_I18N = True
USE_TZ = True

# --- Static & media ---------------------------------------------------------
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_URL = "accounts:login"
LOGIN_REDIRECT_URL = "accounts:profile"
LOGOUT_REDIRECT_URL = "home"

# --- File upload limits -----------------------------------------------------
DATA_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024  # 10 MB

# --- SMS / OTP (kept for a later switch; verification disabled for now) ------
# SMS_BACKEND options: "console" (prints code to logs, free) | "eskiz" | "off"
SMS_BACKEND = os.environ.get("SMS_BACKEND", "off")
PHONE_VERIFICATION_REQUIRED = os.environ.get(
    "PHONE_VERIFICATION_REQUIRED", "False"
).lower() == "true"
ESKIZ_EMAIL = os.environ.get("ESKIZ_EMAIL", "")
ESKIZ_PASSWORD = os.environ.get("ESKIZ_PASSWORD", "")

MESSAGE_TAGS = {
    10: "debug", 20: "info", 25: "success", 30: "warning", 40: "danger",
}

# --- Jazzmin admin theme ----------------------------------------------------
JAZZMIN_SETTINGS = {
    "site_title": "NUBEL Admin",
    "site_header": "NUBEL – Belarus qabul tizimi",
    "site_brand": "NUBEL Qabul",
    "welcome_sign": "NUBEL boshqaruv paneliga xush kelibsiz",
    "copyright": "Nukus davlat texnika universiteti",
    "search_model": ["applications.Application", "accounts.CustomUser"],
    "topmenu_links": [
        {"name": "Sayt", "url": "home", "new_window": True},
        {"model": "accounts.CustomUser"},
        {"model": "applications.Application"},
    ],
    "icons": {
        "accounts.CustomUser": "fas fa-user",
        "auth.Group": "fas fa-users",
        "applications.Application": "fas fa-file-alt",
        "applications.Programme": "fas fa-graduation-cap",
        "applications.Faculty": "fas fa-university",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": True,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-primary",
    "accent": "accent-primary",
    "navbar": "navbar-primary navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
}
