from django.db import models
from django.db import models
from datetime import date
from django.db.models import Max
from .models import *
from setup.models import *


# Create your models here.

class Lifting(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    liftingpayment = models.IntegerField()
    date = models.DateField()


class Sales(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    dsr = models.ForeignKey(Dsr,  on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.CASCADE )
    sales_type = models.CharField(max_length=10, choices=[('psr', 'PSR'), ('holesale', 'Holesale'), ('retail', 'Retail')])
    date = models.DateField()
    salestaka = models.IntegerField()


class Damage(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    dsr = models.ForeignKey(Dsr,  on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.CASCADE )
    date = models.DateField()
    damagetaka = models.FloatField()


class SupplierPayment(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"Payment of {self.amount} to {self.supplier.name} on {self.date} on {self.bank.account_no}"
    def item_type(self):
        return "SupplierPayment"
    

class Dailycost(models.Model):
    dsr = models.ForeignKey(Dsr, on_delete=models.CASCADE)
    date = models.DateField()
    carcost = models.DecimalField(max_digits=10, decimal_places=2) 
    dsrbill = models.DecimalField(max_digits=10, decimal_places=2) 
    toll = models.DecimalField(max_digits=10, decimal_places=2) 
    othercost = models.DecimalField(max_digits=10, decimal_places=2) 
    discription = models.CharField(max_length=1000) 

    def __str__(self):
        return f"  {self.dsr} , {self.carcost}, {self.dsrbill} , {self.toll}, {self.othercost},  {self.date} "
    

class Redamage(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()  # make sure this field exists


class Displaybill (models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class Claim (models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class CollectionTransaction(models.Model):
    collection_man = models.ForeignKey(Collectionsetup, on_delete=models.CASCADE)
    date = models.DateField()
    transaction_type = models.CharField(max_length=10, choices=[('deposit', 'Deposit'), ('withdrawal', 'Withdrawal')])
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2)
