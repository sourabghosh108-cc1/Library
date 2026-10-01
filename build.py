"""Vercel build step: run migrations before deploy (see README for database notes)."""
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cyancom.settings")
django.setup()

from django.core.management import call_command

call_command("migrate", "--noinput")
print("Build: migrations applied.")
