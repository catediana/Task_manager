# api/wsgi.py
import os, sys
from pathlib import Path

# Add repo root to Python path
ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

# Point to Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task_manager_project.settings")

from django.core.wsgi import get_wsgi_application

# Standard Django WSGI application
application = get_wsgi_application()

# Vercel requires a module-level variable named `app`
app = application
