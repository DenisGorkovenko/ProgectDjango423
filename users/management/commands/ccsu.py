import os
from django.core.management import BaseCommand
from dotenv import load_dotenv
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@web.top',
            first_name='admin',
            last_name='adminov',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        load_dotenv()
        user.set_password(os.getenv('SU_PASSWORD'))
        user.save()
        return 'Admin created'
