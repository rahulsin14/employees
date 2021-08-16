from rest_framework import serializers
from .models import employees


class employeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields = (
                  "year_month",
                  "month_of_release",
                  "passenger_type",
                  "direction",
                  "citizenship",
                  "visa",
                  "country_of_residence",
                  "estimate",
                  "standard_error",
                  "status"
        )