set -o errexit

pip install --upgrade pip
pip install --no-cache-dir -r skinvision_backend/requirements.txt
python manage.py collectstatic --no-input

# python manage.py migrate