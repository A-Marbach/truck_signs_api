from .base import *
import os

DEBUG = os.environ.get("DEBUG", "True") == "True"
SECRET_KEY = os.environ.get("SECRET_KEY", "unsafe-secret-for-dev-only")

CORS_ALLOWED_ORIGINS = [
    "https://www.signsfortrucks.com",
    "https://signsfortrucks.com",
    "http://localhost:3000",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("DB_NAME", "trucksigns"),
        'USER': os.environ.get("DB_USER", "user"),
        'PASSWORD': os.environ.get("DB_PASSWORD", "password"),
        'HOST': os.environ.get("DB_HOST", "db"),
        'PORT': int(os.environ.get("DB_PORT", 5432)),
    }
}

STRIPE_PUBLISHABLE_KEY = os.environ.get("STRIPE_PUBLISHABLE_KEY", "")
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", "")

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")
