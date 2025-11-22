import os
from pathlib import Path
from django.core.management.utils import get_random_secret_key


try:
    import dj_database_url
except ImportError:
    dj_database_url = None

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Hosts configuration
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# Custom admin URL for security
DJANGO_ADMIN_URL = os.environ.get('DJANGO_ADMIN_URL', 'admin/')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'education',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'education' / 'templates', 
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

# Database Configuration - ROBUSTA
def get_database_config():
    
    database_url = os.environ.get('DATABASE_URL')
    
    print("🔍 ANALISANDO CONFIGURAÇÃO DO BANCO:")
    print(f"   DATABASE_URL: {'Definida' if database_url else ' Não definida'}")
    
    # Se dj_database_url está disponível e DATABASE_URL existe
    if dj_database_url and database_url:
        try:
            print("Usando dj-database-url")
            return dj_database_url.config(
                conn_max_age=600,
                conn_health_checks=True,
                ssl_require=True
            )
        except Exception as e:
            print(f"Erro no dj-database-url: {e}")
    
    if database_url and ('postgres://' in database_url or 'postgresql://' in database_url):
        print("Tentando conexão PostgreSQL manual")
        try:
            
            url_without_protocol = database_url.replace('postgres://', '').replace('postgresql://', '')
            user_pass, host_port_db = url_without_protocol.split('@')
            user, password = user_pass.split(':')
            host_port, database_with_params = host_port_db.split('/')
            database = database_with_params.split('?')[0]
            
            if ':' in host_port:
                host, port = host_port.split(':')
            else:
                host, port = host_port, '5432'
            
            config = {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': database,
                'USER': user,
                'PASSWORD': password,
                'HOST': host,
                'PORT': port,
                'OPTIONS': {
                    'sslmode': 'require',
                },
            }
            print(f"PostgreSQL configurado: {host}:{port}")
            return config
            
        except Exception as e:
            print(f"Erro no parse PostgreSQL: {e}")
            print("Fallback para SQLite")
    
   
    print(" Usando SQLite (fallback)")
    return {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }

DATABASES = {
    'default': get_database_config()
}

print("TESTANDO CONEXÃO COM O BANCO...")
try:
    # Importação condicional do PostgreSQL
    db_engine = DATABASES['default']['ENGINE']
    
    if 'postgresql' in db_engine:
        # Tenta importar psycopg2
        try:
            import psycopg2
            print("psycopg2 disponível")
        except ImportError:
            print("psycopg2 não instalado. Instale com: pip install psycopg2-binary")
            # Força fallback para SQLite
            DATABASES['default'] = {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
            print("Alternado para SQLite")
    
    # Testa a conexão final
    from django.db import connections
    connection = connections['default']
    connection.ensure_connection()
    print(f"Conexão bem-sucedida com: {DATABASES['default']['ENGINE']}")
    
except Exception as e:
    print(f"Erro na conexão: {e}")
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    print("   🔄 Fallback final para SQLite")

print("=" * 50)

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Security Settings
IS_PRODUCTION = os.environ.get('VERCEL') or os.environ.get('DATABASE_URL') or not DEBUG

if IS_PRODUCTION:
    print("Configurações de PRODUÇÃO ativadas")
    # Security settings for production
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    
    # SSL/HTTPS settings
    SECURE_SSL_REDIRECT = os.environ.get('SECURE_SSL_REDIRECT', 'True') == 'True'
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    
    # Cookie settings
    CSRF_COOKIE_SECURE = os.environ.get('CSRF_COOKIE_SECURE', 'True') == 'True'
    SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE', 'True') == 'True'
    
    # CSRF trusted origins
    CSRF_TRUSTED_ORIGINS = [
        'https://*.vercel.app',
        'https://*.now.sh',
        'https://hmrfvtipkidklknzobhd.supabase.co',
    ]
    
    # Additional production hosts
    additional_hosts = os.environ.get('ADDITIONAL_HOSTS', '')
    if additional_hosts:
        ALLOWED_HOSTS.extend(additional_hosts.split(','))
    
    # Ensure Vercel hosts are included
    ALLOWED_HOSTS.extend(['.vercel.app', '.now.sh'])
    
else:
    print("💻 Configurações de DESENVOLVIMENTO ativadas")
    SECURE_SSL_REDIRECT = False
    CSRF_COOKIE_SECURE = False
    SESSION_COOKIE_SECURE = False
    
    try:
        import debug_toolbar
        INSTALLED_APPS += ['debug_toolbar']
        MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE
        INTERNAL_IPS = ['127.0.0.1']
        print("Debug Toolbar ativado")
    except ImportError:
        print("ℹDebug Toolbar não instalado")

# Custom admin URL security
if DJANGO_ADMIN_URL != 'admin/':
    ADMIN_URL = DJANGO_ADMIN_URL.strip('/')

print("Configuração do Django concluída!")
print("=" * 50)