import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-tu-clave-secreta-aqui'
DEBUG = True

ALLOWED_HOSTS = []

# ---------------------------------------------------
# 1) INSTALLED_APPS: comprueba que están django.contrib.auth y django.contrib.sessions
# ---------------------------------------------------
INSTALLED_APPS = [
    # apps de Django...
    'django.contrib.admin',
    'django.contrib.auth',         # ← obligatorio para autenticación
    'django.contrib.contenttypes',
    'django.contrib.sessions',     # ← obligatorio para sesiones
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # tus apps:
    'clientes',
    'obras',
    'facturacion',
    'contabilidad',
    'usuarios',
]

# ---------------------------------------------------
# 2) MIDDLEWARE: asegúrate de tener AuthenticationMiddleware y SessionMiddleware
# ---------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',       # ← para manejar sesiones
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',    # ← para manejar autenticación
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'crm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',       # incluye datos de usuario en templates
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'crm.wsgi.application'

# ---------------------------------------------------
# 3) LOGIN/LOGOUT REDIRECT: define URLs tras iniciar/cerrar sesión
# ---------------------------------------------------
LOGIN_REDIRECT_URL = 'dashboard'    # al hacer login, redirige a la vista con name="dashboard"
LOGOUT_REDIRECT_URL = 'dashboard'   # al hacer logout, regresa a la misma vista

# 4) (Opcional) Si quieres usar /usuarios/login/ como URL de login
LOGIN_URL = 'login'                  # este debe coincidir con path(name="login") en tus urls

# ---------------------------------------------------
# Base de datos (puedes adaptarla a producción)
# ---------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Idioma y zona horaria
LANGUAGE_CODE = 'es'
TIME_ZONE = 'Europe/Madrid'
USE_I18N = True
USE_TZ = True

# Archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
