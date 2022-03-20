# Generated by Django 3.2.6 on 2022-03-16 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('refer', '0004_auto_20220315_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='recommended_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ref_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
