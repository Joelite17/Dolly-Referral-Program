# Generated by Django 3.2.6 on 2022-03-17 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0017_alter_withdrawalrequest_usdt_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='balance',
        ),
    ]