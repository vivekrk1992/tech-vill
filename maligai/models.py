from django.db import models
from django.contrib.auth.models import User


class Vehicle(models.Model):
    number = models.CharField(max_length=10)
    owner = models.ForeignKey(User)
    insurance_data = models.DateField()

    def __str__(self):
        return self.owner.username


class PickupTrip(models.Model):
    vehicle = models.ForeignKey(Vehicle)
    driver = models.ForeignKey(User)

    odo_start = models.IntegerField(blank=True, null=True)
    odo_end = models.IntegerField(blank=True, null=True)
    date = models.DateField()
    logged_by = models.ForeignKey(User, related_name='logged_by')

    def __str__(self):
        return self.driver.username + self.vehicle.number


class ExpenseType(models.Model):
    name = models.CharField(max_length=30)
    note = models.TextField()

    def __str__(self):
        return self.name


class Expense(models.Model):
    pickup_trip = models.ForeignKey(PickupTrip)
    expense_type = models.ForeignKey(ExpenseType)
    amount = models.DecimalField(max_digits=9, decimal_places=2)


class TripProductCost(models.Model):
    pickup_trip = models.ForeignKey(PickupTrip)
    amount = models.DecimalField(max_digits=9, decimal_places=2)


class PerDayTotalProductCost(models.Model):
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    date = models.DateField()
