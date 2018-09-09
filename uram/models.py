from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13, blank=True, null=True)
    gst_no = models.CharField(max_length=15, blank=True, null=True)
    latitude = models.CharField(max_length=40, blank=True, null=True)
    longitude = models.CharField(max_length=40, blank=True, null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserType(models.Model):
    name = models.CharField(max_length=50)
    notes = models.CharField(max_length=250)
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
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
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    business = models.ForeignKey(Business)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    mobile = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.business.name + ' - ' + self.first_name


class Agency(models.Model):
    business = models.ForeignKey(Business)
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    latitude = models.CharField(max_length=40, blank=True, null=True)
    longitude = models.CharField(max_length=40, blank=True, null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    business = models.ForeignKey(Business)
    name = models.CharField(max_length=100)
    notes = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=20)
    notes = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Stock(models.Model):
    business = models.ForeignKey(Business)
    lot = models.CharField(max_length=10)
    product = models.ForeignKey(Product)
    purchase_quantity = models.PositiveIntegerField()
    available_quantity = models.PositiveIntegerField()
    unit = models.ForeignKey(Unit)
    is_available = models.BooleanField(default=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)


class SaleGroup(models.Model):
    date = models.DateField()
    sale_total_amount = models.PositiveIntegerField()
    discount_amount = models.PositiveIntegerField(default=0)
    borrow_amount = models.PositiveIntegerField(default=0)
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)


class Sale(models.Model):
    sale_group = models.ForeignKey(SaleGroup)
    product = models.ForeignKey(Product)
    stock = models.ForeignKey(Stock)
    customer = models.ForeignKey(Customer)
    quantity = models.PositiveIntegerField()
    unit = models.ForeignKey(Unit)
    rate = models.PositiveIntegerField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)


