# Generated by Django 5.1.1 on 2024-10-06 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0004_alter_branch_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]