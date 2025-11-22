import os
import sys
from django.core.wsgi import get_wsgi_application


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

try:
    application = get_wsgi_application()
    app = application  
    print("Django application loaded successfully!")
except Exception as e:
    print(f"ERROR loading Django: {str(e)}")
    import traceback
    print(f"TRACEBACK: {traceback.format_exc()}")
    
    def app(environ, start_response):
        status = '500 Internal Server Error'
        response_headers = [('Content-type', 'text/plain')]
        start_response(status, response_headers)
        return [b'Django application failed to load']