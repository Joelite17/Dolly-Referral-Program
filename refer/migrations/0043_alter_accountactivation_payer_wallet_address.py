# Generated by Django 3.2.6 on 2022-03-20 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0042_auto_20220320_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountactivation',
            name='Payer_Wallet_Address',
            field=models.CharField(max_length=47),
        ),
    ]
