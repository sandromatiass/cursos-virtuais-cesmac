import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

import django
django.setup()

from django.conf import settings
from django.db import connection

db = settings.DATABASES['default']
print("🔍 BANCO DE DADOS ATUAL:")
print(f"   Engine: {db['ENGINE']}")
print(f"   Name: {db['NAME']}")

if 'postgresql' in db['ENGINE']:
    print("Conectado ao POSTGRESQL (Vercel/Supabase)")
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print(f"PostgreSQL: {version[0]}")
else:
    print("Conectado ao SQLITE (Local)")