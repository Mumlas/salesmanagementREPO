# Generated by Django 5.1.1 on 2024-10-23 14:42

import authUser.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authUser', '0009_alter_user_name'),
        ('setup', '0014_alter_price_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_staff', to='setup.staff'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=11, unique=True, validators=[authUser.models.validate_phone], verbose_name='phone number'),
        ),
    ]