# Generated by Django 4.2.7 on 2023-11-05 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0009_alter_hotel_image_alter_room_image_alter_user_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='capacity',
        ),
    ]