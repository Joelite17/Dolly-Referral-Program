# Generated by Django 3.2.6 on 2022-03-16 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('refer', '0005_alter_profile_recommended_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountactivation',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
