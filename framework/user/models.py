from django.db import models
from django.contrib.auth.models import AbstractUser
from framework.utils import GENDER_CHOICES
from framework.utils import EDUCATIONAL_INSTITUTION_TYPE 

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

class EducationInstitution(models.Model):

    name = models.CharField(max_length=50, blank=False, null=False)
    slug = models.SlugField(unique=True)
    isVerified = models.BooleanField(blank=False, null=True, default=False)
    type = models.PositiveSmallIntegerField(choices=EDUCATIONAL_INSTITUTION_TYPE, default=0)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        db_table = 'education_institution'
        verbose_name = 'Education Institution'
        verbose_name_plural = 'Education Institutions'
    
    def __str__(self):
        return self.name



__all__ = [
    'User',
    'EducationInstitutio'
] 


