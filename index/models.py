"""
The script describes the project models

created by: Pinchukov Artur
date: 13.10.17
"""

# standard libs
import random
import string
# frameworks
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

# static data
SECRET_KEY_SIZE = 32
KEY_STATUS = (
    ('No active', 'No active'),
    ('Expired', 'Expired'),
    ('Active', 'Active'),
)


def gen_secret_key():
    """
    The method create random secret key
    :return: str secret key
    """
    key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
                  for x in range(SECRET_KEY_SIZE))
    return key


def get_date_now():
    """
    The method return datetime now
    :return: now datetime
    """
    return timezone.now()


class LevelFile(models.Model):
    """
    Model file level
    """
    level_name = models.CharField(primary_key=True, max_length=35, null=False, verbose_name="Level Name",
                                  help_text="max size: 35", )
    level_file = models.FileField(null=False, blank=False, upload_to="levels/", verbose_name="File script", )
    keys = models.ManyToManyField('TestSecretKey', blank=True)
    level_pub_date = models.DateTimeField(null=False, default=get_date_now)

    def __str__(self):
        return self.level_name

    class Meta:
        ordering = ('level_name',)


class TestSecretKey(models.Model):
    """
    Model secret key provided to each level tester
    """
    title = models.CharField(max_length=35, null=True, verbose_name="Title", default="", help_text="max size: 35",)
    secret_key = models.CharField(primary_key=True, max_length=SECRET_KEY_SIZE, null=False, verbose_name="Secret Key",
                                  default=gen_secret_key)
    lifetime = models.IntegerField(validators=[MaxValueValidator(1000), MinValueValidator(1)], null=False,
                                   verbose_name="Lifetime(days)", help_text="max size: 1000", )
    status = models.CharField(max_length=10, choices=KEY_STATUS, null=False, verbose_name="Status", default="No active")
    levels = models.ManyToManyField(LevelFile, through=LevelFile.keys.through, blank=True)
    key_pub_date = models.DateTimeField(null=False, default=get_date_now, verbose_name="key release date",)
    key_active_date = models.DateTimeField(null=True, verbose_name="key activation date",)

    def __str__(self):
        return self.secret_key

    class Meta:
        ordering = ('secret_key',)
