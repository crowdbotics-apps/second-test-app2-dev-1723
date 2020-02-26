from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=255,)
    username = models.CharField(max_length=100, null=True, blank=True,)
    email = models.EmailField(max_length=254, null=True, blank=True,)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
