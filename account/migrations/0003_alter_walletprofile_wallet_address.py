# Generated by Django 3.2.6 on 2022-03-15 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20220315_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walletprofile',
            name='wallet_address',
            field=models.CharField(max_length=15),
        ),
    ]
