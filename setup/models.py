from django.db import models

# Create your models here.


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    balance = models.FloatField()

    def __str__(self):
        return self.name
    

class Market(models.Model):
    area = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.address
    


class Bank(models.Model):
    BANK_TYPE_CHOICES = (
        ('Deposit', 'Deposit A/c'),
        ('CC', 'CC A/c'),
    )
    bank_name = models.CharField(max_length=50)
    account_no = models.CharField(max_length=20)
    branch = models.CharField(max_length=50)
    account_type = models.CharField(max_length=10, choices=BANK_TYPE_CHOICES, default='Deposit')

    def __str__(self):
        return self.bank_name
    


class Dsr(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Salesmanager(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Collectionsetup(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name