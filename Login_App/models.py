from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    fullname = models.CharField(max_length=200, blank=False)
    profile_pic = models.ImageField(upload_to='profile_picture')

    sex = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('SheMale', 'SheMale'),
    )

    zender = models.CharField(max_length=2, choices=sex)

    def __str__(self):
        return self.user.username
