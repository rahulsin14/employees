from django.db import models


# Create your models here.
class employees(models.Model):
    year_month = models.CharField(max_length=100)
    month_of_release = models.CharField(max_length=100)
    passenger_type = models.CharField(max_length=100)
    direction= models.CharField(max_length=100)
    citizenship= models.CharField(max_length=100)
    visa= models.CharField(max_length=100)
    country_of_residence= models.CharField(max_length=100)
    estimate= models.CharField(max_length=100)
    standard_error= models.CharField(max_length=100)
    status= models.CharField(max_length=100)

    def __str__(self):
        return self.year_month

