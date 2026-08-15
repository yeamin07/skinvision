#!/bin/bash
set -o errexit

pip install --upgrade pip
pip install --no-cache-dir -r skinvision_backend/requirements.txt

# Change to the Django project directory
cd skinvision_backend

python manage.py collectstatic --no-input
# python manage.py migrate

# python manage.py migrate