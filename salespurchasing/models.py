from django.db import models

from utils.models import Timestamp, auto_number


class Product(Timestamp):
    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=20)
    sales_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(max_length=10, default=0)

    def __str__(self):
        return self.sku


class Expense(Timestamp):
    expense_date = models.DateField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.expense_date)


class ExpenseItem(Timestamp):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    description = models.CharField(max_length=225)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.description


class Supplier(Timestamp):
    supplier_code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.supplier_code


class Purchase(Timestamp):
    purchase_number = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    purchase_date = models.DateField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    pay = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    change = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.purchase_number


class PurchaseItem(Timestamp):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    quantity = models.PositiveIntegerField(default=1)
    total = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product.name


class SalesOrder(Timestamp):
    order_number = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    order_date = models.DateField()
    total = models.PositiveIntegerField(default=0)
    pay = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    change = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.order_number


class OrderItem(Timestamp):
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sales_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    quantity = models.PositiveIntegerField(default=1)
    total = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product.name


