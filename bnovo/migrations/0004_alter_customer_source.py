# Generated by Django 5.0.2 on 2024-03-23 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnovo', '0003_alter_customer_email_alter_customer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='source',
            field=models.CharField(max_length=200, verbose_name='Источник бронирования'),
        ),
    ]