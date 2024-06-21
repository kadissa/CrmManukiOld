# Generated by Django 5.0.2 on 2024-03-08 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webhooks', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='customer',
            constraint=models.UniqueConstraint(fields=('booking_id', 'status'), name='unique_booking_id_status'),
        ),
    ]