# Generated by Django 5.0.2 on 2024-03-24 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnovo', '0007_customer_real_arrival_customer_real_departure_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='real_arrival',
            field=models.CharField(max_length=40, verbose_name='Время заезда'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='real_departure',
            field=models.CharField(max_length=40, verbose_name='Время выезда'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='room_id',
            field=models.CharField(max_length=40, verbose_name='Номер Домика'),
        ),
    ]