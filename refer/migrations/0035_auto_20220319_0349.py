# Generated by Django 3.2.6 on 2022-03-19 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0034_profile_pending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='earn',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pending',
            field=models.IntegerField(default=0),
        ),
    ]
