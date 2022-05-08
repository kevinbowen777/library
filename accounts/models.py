from django.contrib.auth.models import AbstractUser, Group
from django.db import models  # noqa:F401

library_members, created = Group.objects.get_or_create(name="Library Members")
librarians, created = Group.objects.get_or_create(name="Librarians")


class CustomUser(AbstractUser):
    pass
