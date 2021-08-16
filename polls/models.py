from django.db import models


# Create your models here.
class employees(models.Model):
    year_month = models.CharField(max_length=2)
    month_of_release = models.CharField(max_length=2)
    passenger_type = models.CharField(max_length=2)
    direction= models.CharField(max_length=2)
    citizenship= models.CharField(max_length=2)
    visa= models.CharField(max_length=2)
    country_of_residence= models.CharField(max_length=2)
    estimate= models.CharField(max_length=2)
    standard_error= models.CharField(max_length=2)
    status= models.CharField(max_length=2)

    def __str__(self):
        return self.year_month
