#!/usr/bin/env bash
set -e

export DJANGO_SETTINGS_MODULE=truck_signs_designs.settings.production

echo "Waiting for PostgreSQL to be available..."
while ! nc -z db 5432; do
  sleep 0.1
done

echo "PostgreSQL is up - continuing..."

python manage.py collectstatic --noinput
python manage.py migrate

echo "👤 Creating Django superuser if it doesn't exist..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
username = "${DJANGO_SUPERUSER_USERNAME}"
email = "${DJANGO_SUPERUSER_EMAIL}"
password = "${DJANGO_SUPERUSER_PASSWORD}"
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser '{username}' created successfully.")
else:
    print(f"Superuser '{username}' already exists — skipping creation.")
END

echo "🚀 Starting Gunicorn..."
exec gunicorn truck_signs_designs.wsgi:application --bind 0.0.0.0:8020