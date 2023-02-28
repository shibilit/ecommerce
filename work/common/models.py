from django.db import models

# Create your models here.


class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    e_mail = models.CharField(max_length=50)
    ph_number = models.CharField(max_length=30)
    address = models.CharField(max_length=500)
    password = models.CharField(max_length=20)
    image = models.ImageField(upload_to='customer/')

    class Meta:
        db_table = 'customer'


class Seller(models.Model):
    seller_name = models.CharField(max_length=20)
    company_name = models.CharField(max_length=50)
    acc_no = models.BigIntegerField()
    ifsc = models.CharField(max_length=50)
    branch_name = models.CharField(max_length=50)
    acc_holder_name = models.CharField(max_length=50)
    ph_num = models.BigIntegerField()
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='seller/')
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = 'seller_tb'
