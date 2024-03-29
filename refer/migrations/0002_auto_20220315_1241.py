# Generated by Django 3.2.6 on 2022-03-15 19:41

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('refer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='wallet_address',
        ),
        migrations.RemoveField(
            model_name='withdrawalrequest',
            name='USDT_Address',
        ),
        migrations.AddField(
            model_name='withdrawalrequest',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='refer.profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='withdrawalrequest',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='withdrawalrequest',
            name='USDT_Amount',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(20, 'Minimum_Withdrawal $20')]),
        ),
    ]
