# Generated by Django 5.1.1 on 2024-10-06 14:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0005_alter_storage_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_updated',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]