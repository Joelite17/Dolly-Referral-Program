# Generated by Django 3.2.6 on 2022-03-15 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_walletprofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='walletprofile',
            name='wallet_address',
        ),
    ]
