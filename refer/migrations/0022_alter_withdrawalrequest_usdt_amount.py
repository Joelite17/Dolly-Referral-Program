# Generated by Django 3.2.6 on 2022-03-18 06:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0021_alter_profile_total_earning'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawalrequest',
            name='USDT_Amount',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1, 'Minimum_Withdrawal $20')]),
        ),
    ]
