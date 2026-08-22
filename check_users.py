import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

print("📋 All users:")
for u in User.objects.all():
    print(f"  - {u.username} (admin: {u.is_superuser})")

print(f"\n✅ Total users: {User.objects.count()}")