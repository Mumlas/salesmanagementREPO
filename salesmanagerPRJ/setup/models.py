from django.db import models
from datetime import date
# Create your models here.

class Branch(models.Model):
    branchName = models.CharField(max_length=200, unique=True)
    branchAddress = models.CharField(max_length=200, null=False)

    class Meta:
        verbose_name_plural="Branches"

    def __str__(self):
        return(self.branchName)
    
class Storage(models.Model):
    storageDesc = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    branch = models.ForeignKey(Branch,related_name='storage_branch', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural="Storage"

    def __str__(self):
        return(self.storageDesc)
    
class Product(models.Model):
    type = models.CharField(max_length=100, unique=True)
    storage = models.ForeignKey(Storage, related_name='product_storage', on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, null=False, unique=False, default=0)
    date_updated = models.DateField(default=date.today)

    class Meta:
        verbose_name_plural="Products"

    def __str__(self):
        return(self.type)
    
class Pump(models.Model):
    pupmDesc = models.CharField(max_length=100)
    storage = models.ForeignKey(Storage, related_name='pump_storage', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural="Pump"

    def __str__(self):
        return(self.pupmDesc)
    
# Staff
class Staff(models.Model):
    title = models.CharField(max_length=20)
    firstname = models.CharField(max_length=50, db_index=True)
    surname = models.CharField(max_length=50, db_index=True)
    dateofbirth = models.DateField()
    employmentdate = models.DateField()
    designation = models.CharField(max_length=30, db_index=True)
    branch = models.ForeignKey(Branch, related_name='staff_branch', on_delete=models.CASCADE)
    email = models.EmailField(unique=True, null=True)
    phonenumber = models.IntegerField(unique=True, null=False)

    class Meta:
        verbose_name_plural="Staff"

    def __str__(self):
        return(self.firstname, +" "+ self.surname)
    
class Shift(models.Model):
    type = models.CharField(max_length=20, unique=True, null=False)
    start = models.DateTimeField(unique=True, null=False)
    end = models.DateTimeField(unique=True, null=False)

    class Meta:
        verbose_name_plural="Shift"

    def __str__(self):
        return(self.type)