#!/bin/bash

echo "Starting Django application..."

# Run migrations
echo "Running migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start server
echo "Starting Django server..."
if [ "$DJANGO_DEBUG" = "True" ]; then
  echo "Running in DEBUG mode with runserver..."
  python manage.py runserver 0.0.0.0:8000
else
  echo "Running in production mode with Gunicorn..."
  gunicorn GreatKart.wsgi:application --bind 0.0.0.0:8000 --workers 3
fi