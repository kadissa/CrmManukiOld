# Generated by Django 5.0.2 on 2024-04-07 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webhooks', '0013_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='rotenburo_1',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Ротенбуро'),
        ),
    ]
