import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moneytransfer.settings")
django.setup()

from django.contrib.auth.models import User
from core.models import UserProfile

# Create 10 test users
for i in range(1, 101):
    username = f"user{i}"
    password = "test1234"
    balance = 1000.00

    if not User.objects.filter(username=username).exists():
        user = User.objects.create_user(username=username, password=password)
        UserProfile.objects.create(user=user, balance=balance)
        print(f"✅ Created: {username}")
    else:
        print(f"⚠️ Skipped (already exists): {username}")

# Create 1 test user
# username = ""
# password = ""
# balance = 1000.00

# if not User.objects.filter(username=username).exists():
#     user = User.objects.create_user(username=username, password=password)
#     UserProfile.objects.create(user=user, balance=balance)
#     print(f"✅ Created: {username}")
# else:
#     print(f"⚠️ Skipped (already exists): {username}")