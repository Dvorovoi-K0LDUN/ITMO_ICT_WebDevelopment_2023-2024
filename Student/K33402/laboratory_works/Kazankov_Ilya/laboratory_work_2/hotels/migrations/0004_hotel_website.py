# Generated by Django 4.2.7 on 2023-11-04 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_alter_hotel_phone_alter_hotel_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='website',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
