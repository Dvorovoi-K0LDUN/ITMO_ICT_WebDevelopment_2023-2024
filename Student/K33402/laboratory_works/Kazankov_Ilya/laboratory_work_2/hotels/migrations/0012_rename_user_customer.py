# Generated by Django 4.2.7 on 2023-11-05 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0011_booking_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Customer',
        ),
    ]
