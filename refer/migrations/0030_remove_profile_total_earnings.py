# Generated by Django 3.2.6 on 2022-03-18 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0029_auto_20220318_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='total_earnings',
        ),
    ]