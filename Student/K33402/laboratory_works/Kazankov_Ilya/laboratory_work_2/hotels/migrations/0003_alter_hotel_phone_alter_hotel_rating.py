# Generated by Django 4.2.7 on 2023-11-04 13:48

import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_alter_hotel_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='rating',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]