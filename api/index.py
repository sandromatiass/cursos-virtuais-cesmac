import os
import sys
from django.core.wsgi import get_wsgi_application


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

try:
    application = get_wsgi_application()
except Exception as e:
   
    print(f"Error starting Django: {e}")
    raise