import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from django.core.management import call_command

print("🔄 Running migrations...")
call_command('makemigrations')
call_command('migrate')

print("✅ Database migrations completed!")