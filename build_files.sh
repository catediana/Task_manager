#!/usr/bin/env bash
set -e

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
#pip install -r requirements.txt

# Collect static files into STATIC_ROOT
python manage.py collectstatic --noinput

# (Optional) Run migrations if you’ve set DATABASE_URL in Verc
if [ -n "$DATABASE_URL" ]; then
  python manage.py migrate --noinput
fi
