import os
import sys
from django.core.wsgi import get_wsgi_application

# Adiciona o path do projeto
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

try:
    application = get_wsgi_application()
    print(" Django application loaded successfully!")
except Exception as e:
    print(f"ERROR loading Django: {str(e)}")
    print(f"ERROR type: {type(e).__name__}")
    import traceback
    print(f"TRACEBACK: {traceback.format_exc()}")
    raise