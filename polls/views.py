from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from . serializers import employeesSerializer
import json
import csv

class employeeList(APIView):

    def get(self, request):
        employees1=employees.objects.all()
        serializer=employeesSerializer(employees1, many=True)
        return Response(serializer.data)

    def post(self,request):
        data =self.make_json("/home/rahul/Downloads/international-migration-March-2021-citizenship-by-visa-by-country-of-last-permanent-residence (1).csv")
        serializer = employeesSerializer(data=data,many=True)
        # print(request.data)
        if serializer.is_valid():
            serializer.save()
            # print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def make_json(self,csvFilePath):
        # create a dictionary
        data = []

        # Open a csv reader called DictReader
        with open(csvFilePath, encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)

            # Convert each row into a dictionary
            # and add it to data
            for rows in csvReader:
                # Assuming a column named 'No' to
                # be the primary key
                # key = rows['Emp ID']
                # data[key] = rows
                data.append(rows)

        return data

