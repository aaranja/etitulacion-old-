# Generated by Django 2.2.7 on 2019-12-10 22:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20191210_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminprofile',
            name='account',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='graduateprofile',
            name='account',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='graduate_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]