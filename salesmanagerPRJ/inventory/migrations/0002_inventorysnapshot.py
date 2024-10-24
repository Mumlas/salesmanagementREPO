# Generated by Django 5.1.1 on 2024-10-10 21:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
        ('setup', '0008_storage_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventorySnapShot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('date', models.DateField()),
                ('inventoryv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventory')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.product')),
            ],
            options={
                'verbose_name_plural': 'Inventory',
            },
        ),
    ]
