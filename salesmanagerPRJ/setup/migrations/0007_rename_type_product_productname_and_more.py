# Generated by Django 5.1.1 on 2024-10-08 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0006_product_date_updated_product_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='type',
            new_name='productName',
        ),
        migrations.RenameField(
            model_name='storage',
            old_name='quantity',
            new_name='capacity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='storage',
        ),
        migrations.AddField(
            model_name='product',
            name='productDescription',
            field=models.CharField(default='None', max_length=200, null=True),
        ),
    ]