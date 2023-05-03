from django.core.management.base import BaseCommand
from authentication.domain import User
from datetime import datetime
from django.contrib.auth.models import UserManager

class Command(BaseCommand):
    help = 'help text'

    def handle(self, *args, **options):
      
      for user in range(1,4):
        username = "nikolas" + str(user)
        email = username + "@gmail.com"
        password = "abcd.1234"

        if not email:
          raise ValueError('Users must have an email address')

        now = datetime.now()
        email = UserManager.normalize_email(email)

        user = User(
          username=username,
          email=email,
          is_staff=False,
          is_active=True,
          is_superuser=False,
          last_login=now,
          date_joined=now,
          identification='1075262622'
        )

        user.set_password(password)
        user.save()