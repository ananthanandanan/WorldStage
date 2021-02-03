from django.db import models
from django.contrib.auth.models import AbstractUser
from framework.utils import GENDER_CHOICES

class User(AbstractUser):
    id = models.BigAutoField(primary_key=True, null=False)
    # email address of the user
    email = models.EmailField(unique=True, null=False, blank=False)
    phone = models.CharField(max_length=15, blank=True, null=True)
    # varchar(255), stores user's first name
    first_name = models.CharField(max_length=255, default='', blank=True, verbose_name='First Name')
    # varchar(255), stores user's last name
    last_name = models.CharField(max_length=255, default='', blank=True, verbose_name='Last Name')
    # varchar(255), a short self-written bio of the user that will be shown in users' profile
    bio = models.CharField(max_length=255, default='', blank=True, verbose_name='Bio')
    # Demographic Data
    birthday = models.DateField(null=True, blank=True)
    # gender of the user, should not be shown publicly on profile
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True,  blank=True)
    # residence location of the user
    city = models.CharField(max_length=127, default='', blank=True)
    state = models.CharField(max_length=127, default='', blank=True)
    country = models.CharField(max_length=10, null=False, blank=False, default='IND')



__all__ = [
    'User',
]


