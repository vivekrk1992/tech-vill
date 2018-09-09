from django.db import models
from django.contrib.auth.models import User


class UserType(models.Model):
    name = models.CharField(max_length=30)
    notes = models.TextField()

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='main_user')
    user_type = models.ForeignKey(UserType, null=True, blank=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    street = models.TextField(blank=True, null=True)
    village = models.CharField(max_length=100, blank=True, null=True)
    taluk = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    latitude = models.CharField(max_length=40, blank=True, null=True)
    longitude = models.CharField(max_length=40, blank=True, null=True)
    mobile = models.BigIntegerField(blank=True, null=True)
    alternate_mobile = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username
