from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=255,)
    username = models.CharField(null=True, blank=True, max_length=100,)
    email = models.EmailField(null=True, blank=True, max_length=254,)
    birth_date = models.DateField(null=True, blank=True,)
    test = models.BigIntegerField(null=True, blank=True,)
    test12345 = models.BigIntegerField(null=True, blank=True,)
    testmore = models.DecimalField(
        null=True, blank=True, max_digits=30, decimal_places=10,
    )
    anothertest = models.IntegerField(null=True, blank=True,)
    test57435 = models.DurationField(null=True, blank=True,)
    anotherfinal = models.SmallIntegerField(null=True, blank=True,)
    final = models.SmallIntegerField(null=True, blank=True,)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
