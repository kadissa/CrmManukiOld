# Generated by Django 5.0.2 on 2024-03-10 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webhooks', '0002_customer_unique_booking_id_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='booking_id',
            field=models.CharField(db_index=True, max_length=60),
        ),
    ]