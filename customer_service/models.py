from django.db import models

class AllCustomerData(models.Model):
    bill_number = models.IntegerField()
    cust_name = models.CharField(max_length=100)
    cust_address = models.TextField()
    cust_number = models.IntegerField()
    cust_email = models.EmailField()

class WebCustomersData(models.Model):
    bill_number = models.IntegerField()
    user_name = models.CharField(max_length=100)
    user_address = models.TextField()
    user_number = models.IntegerField()
    user_email = models.EmailField()
    user_pass = models.CharField(max_length=100)

class ServiceRequestData(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    )

    bill_number = models.IntegerField()
    user_name = models.CharField(max_length=100)
    user_address = models.TextField()
    user_number = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    req_date = models.DateField()
    req_title = models.CharField(max_length=100)
    req_description = models.TextField()
