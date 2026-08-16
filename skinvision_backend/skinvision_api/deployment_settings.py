import os 
import dj_database_url
from .settings import *
from .settings import BASE_DIR

# NEW (hardcoded - works!)
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'https://skinvision-frontend-production.up.railway.app',
]

CSRF_TRUSTED_ORIGINS = ['https://'+os.environ.get('RAILWAY_PUBLIC_DOMAIN')]

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

# Use Railway frontend URL from environment variable
CORS_ALLOWED_ORIGINS = [
    'https://' + os.environ.get('RAILWAY_FRONTEND_DOMAIN', 'localhost:3000'),
]

STORAGES = {
    "default":{
        "BACKEND" : "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND" : "whitenoise.storage.CompressedStaticFilesStorage",
    },

}