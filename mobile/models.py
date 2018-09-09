from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30)
    is_sale_product = models.BooleanField(default=False)
    notes = models.TextField()

    def __str__(self):
        return self.name


class ProductUnit(models.Model):
    name = models.CharField(max_length=10)
    notes = models.TextField()

    def __str__(self):
        return self.name


class ProductBuyingDestination(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    latitude = models.CharField(max_length=40, blank=True, null=True)
    longitude = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.name + self.city


class Trip(models.Model):
    product_buying_destination = models.ForeignKey(ProductBuyingDestination)
    date = models.DateField()

    def __str__(self):
        return self.product_buying_destination.name + ' - ' + str(self.date)


class TripExpenseType(models.Model):
    name = models.CharField(max_length=50)
    notes = models.TextField()

    def __str__(self):
        return self.name


class TripBuyingExpense(models.Model):
    trip = models.ForeignKey(Trip)
    trip_expense_type = models.ForeignKey(TripExpenseType)
    amount = models.DecimalField(max_digits=9, decimal_places=2)


class ProductInventory(models.Model):
    trip = models.ForeignKey(Trip)
    product = models.ForeignKey(Product)
    unit = models.ForeignKey(ProductUnit)
    purchase_quantity = models.IntegerField()
    purchase_date = models.DateField()
    available_quantity = models.IntegerField()
    expiry_date = models.DateField()
    is_over = models.FloatField(default=False)
    date_over = models.DateField()


class ServiceStatus(models.Model):
    name = models.CharField(max_length=30)
    notes = models.TextField()

    def __str__(self):
        return self.name


class ServiceProduct(models.Model):
    name = models.CharField(max_length=30)
    notes = models.TextField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=25)
    village = models.CharField(max_length=30)
    mobile = models.CharField(max_length=13)


class ServiceReceivedCostStatus(models.Model):
    name = models.CharField(max_length=30)
    notes = models.TextField()

    def __str__(self):
        return self.name


class ServiceInventory(models.Model):
    service_product = models.ForeignKey(ServiceProduct)
    customer = models.ForeignKey(Customer)
    date_admit = models.DateTimeField()
    service_status = models.ForeignKey(ServiceStatus)
    is_dispatched = models.BooleanField(default=False)
    date_dispatched = models.DateTimeField(blank=True, null=True)
    service_cost = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    received_cost = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    received_cost_status = models.ForeignKey(ServiceReceivedCostStatus)
    is_transaction_over = models.BooleanField(default=False)


class ServiceIngredient(models.Model):
    service_inventory = models.ForeignKey(ServiceInventory)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    product_unit = models.ForeignKey(ProductUnit)
