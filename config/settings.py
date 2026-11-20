"""Django settings for config project."""

import os
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(DEBUG=(bool, False))

# Settings come from environment variables. A local .env file is optional.
root_env = BASE_DIR / ".env"
if root_env.exists():
    env.read_env(root_env)
environment = os.getenv("DJANGO_ENV", "local").lower()

# In production set DJANGO_SECRET_KEY in .env (long random string). Never commit .env.
SECRET_KEY = env("DJANGO_SECRET_KEY",
                 default="django-insecure-development-key-change-in-production")
DEBUG = env.bool("DJANGO_DEBUG", default=True)
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=[
                         "localhost", "127.0.0.1"])
CSRF_TRUSTED_ORIGINS = env.list("DJANGO_CSRF_TRUSTED_ORIGINS", default=[])

# Local dev: always allow localhost so runserver never returns 400
if environment != "production":
    _local_hosts = {"localhost", "127.0.0.1"}
    ALLOWED_HOSTS = list(_local_hosts | set(ALLOWED_HOSTS))
    _local_csrf = {"http://127.0.0.1:8000", "http://localhost:8000"}
    CSRF_TRUSTED_ORIGINS = list(_local_csrf | set(CSRF_TRUSTED_ORIGINS))

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    "core",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = True
    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_HTTPONLY = True
    SECURE_HSTS_SECONDS = 3600
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = False
    # HSTS preload is a long-term promise for the whole domain and is not needed here,
    # so its deploy-check warning is silenced on purpose.
    SILENCED_SYSTEM_CHECKS = ["security.W021"]
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = "DENY"
    SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'core.context_processors.lang_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# The site has no database: all content lives in core/site_data.py.
DATABASES = {}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
WHITENOISE_MAX_AGE = 31536000
