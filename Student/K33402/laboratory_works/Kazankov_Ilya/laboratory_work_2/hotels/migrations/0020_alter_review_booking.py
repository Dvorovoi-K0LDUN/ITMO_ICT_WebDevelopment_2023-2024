# Generated by Django 4.2.7 on 2023-11-06 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0019_review_id_alter_review_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='booking',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='hotels.booking'),
        ),
    ]
