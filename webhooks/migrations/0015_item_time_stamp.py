# Generated by Django 5.0.2 on 2024-04-07 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webhooks', '0014_alter_guest_rotenburo_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
    ]
