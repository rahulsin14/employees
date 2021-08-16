from django.db import models


# Create your models here.
class employees(models.Model):
    year_month = models.CharField(max_length=255)
    month_of_release = models.CharField(max_length=255)
    passenger_type = models.CharField(max_length=255)
    direction= models.CharField(max_length=255)
    citizenship= models.CharField(max_length=255)
    visa= models.CharField(max_length=255)
    country_of_residence= models.CharField(max_length=255)
    estimate= models.CharField(max_length=255)
    standard_error= models.CharField(max_length=255)
    status= models.CharField(max_length=255)

    def __str__(self):
        return self.year_month
