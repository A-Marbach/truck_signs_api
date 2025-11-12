from .base import *
import os
import environ


env = environ.Env()
environ.Env.read_env(env_file='/app/.env')

# --- Security ---
DEBUG = os.environ.get("DEBUG", "False") == "True"
SECRET_KEY = os.environ.get("SECRET_KEY", "unsafe-secret-for-dev-only")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("DOCKER_DB_NAME"),
        'USER': os.environ.get("DOCKER_DB_USER"),
        'PASSWORD': os.environ.get("DOCKER_DB_PASSWORD"),
        'HOST': os.environ.get("DOCKER_DB_HOST", "db"),
        'PORT': int(os.environ.get("DOCKER_DB_PORT", 5432)),
    }
}

# --- Stripe ---
STRIPE_PUBLISHABLE_KEY = os.environ.get("DOCKER_STRIPE_PUBLISHABLE_KEY", os.environ.get("STRIPE_PUBLISHABLE_KEY", ""))
STRIPE_SECRET_KEY = os.environ.get("DOCKER_STRIPE_SECRET_KEY", os.environ.get("STRIPE_SECRET_KEY", ""))

# --- Email ---
EMAIL_HOST = os.environ.get("DOCKER_EMAIL_HOST", os.environ.get("EMAIL_HOST", "smtp.gmail.com"))
EMAIL_PORT = int(os.environ.get("DOCKER_EMAIL_PORT", os.environ.get("EMAIL_PORT", 587)))
EMAIL_HOST_USER = os.environ.get("DOCKER_EMAIL_HOST_USER", os.environ.get("EMAIL_HOST_USER", ""))
EMAIL_HOST_PASSWORD = os.environ.get("DOCKER_EMAIL_HOST_PASSWORD", os.environ.get("EMAIL_HOST_PASSWORD", ""))
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# --- Cloudinary ---
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUD_NAME', ''),
    'API_KEY': os.environ.get('CLOUD_API_KEY', ''),
    'API_SECRET': os.environ.get('CLOUD_API_SECRET', ''),
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# --- CORS ---
CORS_ALLOWED_ORIGINS = [
    "https://truck-signs-frontend-nextjs-4f1tbf3c3-ceci-aguilera.vercel.app",
    "https://truck-signs-frontend-nextjs.vercel.app",
    "https://truck-signs-frontend-nextjs-git-vercelpre-ceci-aguilera.vercel.app",
]

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

CURRENT_ADMIN_DOMAIN = os.environ.get("CURRENT_ADMIN_DOMAIN", "")
EMAIL_ADMIN = os.environ.get("EMAIL_ADMIN", "")