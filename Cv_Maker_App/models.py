from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CvMaker(models.Model):
    fullname = models.CharField(
        max_length=200, verbose_name='own name', blank=False)
    email = models.EmailField(blank=False)
    phone_number = models.CharField(max_length=12)
    cv_picture = models.ImageField(upload_to='picture', blank=False)
    website = models.URLField(blank=True)
    present_adress = models.CharField(max_length=250, blank=False)
