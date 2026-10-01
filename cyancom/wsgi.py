import os

from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cyancom.settings")

if os.environ.get("VERCEL"):
    try:
        call_command("migrate", "--noinput")
    except Exception:
        pass

application = get_wsgi_application()
