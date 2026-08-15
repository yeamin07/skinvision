set -o errexit

pip install -r skinvision_backend/requirements.txt

python manage.py collectstatic --no-input

# python manage.py migrate