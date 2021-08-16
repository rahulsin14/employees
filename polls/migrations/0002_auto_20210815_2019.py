# Generated by Django 3.2.6 on 2021-08-15 20:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='age',
            new_name='emp_id',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='last_name',
        ),
        migrations.AddField(
            model_name='employees',
            name='lastname',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]
