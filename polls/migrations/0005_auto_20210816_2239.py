# Generated by Django 3.2.6 on 2021-08-16 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20210816_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='citizenship',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employees',
            name='country_of_residence',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employees',
            name='direction',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employees',
            name='estimate',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employees',
            name='month_of_release',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employees',
            name='passenger_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employees',
            name='standard_error',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employees',
            name='status',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employees',
            name='visa',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employees',
            name='year_month',
            field=models.CharField(max_length=100),
        ),
    ]
