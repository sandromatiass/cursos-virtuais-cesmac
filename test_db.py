import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

try:
    import django
    django.setup()
    
    from django.db import connection
    
    print("TESTE DE CONEXÃO SIMPLIFICADO")
    print("=" * 40)
    
    # Tenta conectar
    connection.ensure_connection()
    print("Conexão bem-sucedida!")
    
    # Mostra informações
    from django.conf import settings
    db = settings.DATABASES['default']
    print(f"Engine: {db['ENGINE']}")
    print(f" Database: {db['NAME']}")
    
    if 'postgresql' in db['ENGINE']:
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(f"PostgreSQL: {version[0]}")
    
except Exception as e:
    print(f"Erro: {e}")