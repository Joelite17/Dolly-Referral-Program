# Generated by Django 3.2.6 on 2022-03-15 07:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountActivation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payer_Wallet_Address', models.CharField(max_length=15, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Disapprove'), (1, 'Approve')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='WithdrawalRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USDT_Amount', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1, 'Amount is less than 1'), django.core.validators.MaxValueValidator(20, 'Maximum_Withdrawal $20')])),
                ('USDT_Address', models.CharField(max_length=15)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True)),
                ('code', models.CharField(blank=True, max_length=12)),
                ('wallet_address', models.CharField(max_length=15)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('recommended_by', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ref_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
