import os 
import dj_database_url
from .settings import *
from .settings import BASE_DIR

# Hardcoded CORS (keep this only)
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'https://skinvision-frontend-production.up.railway.app',
]

# Also fix CSRF_TRUSTED_ORIGINS (same issue)
CSRF_TRUSTED_ORIGINS = [
    'https://skinvision-backend-production.up.railway.app',
]

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STORAGES = {
    "default":{
        "BACKEND" : "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND" : "whitenoise.storage.CompressedStaticFilesStorage",
    },
}