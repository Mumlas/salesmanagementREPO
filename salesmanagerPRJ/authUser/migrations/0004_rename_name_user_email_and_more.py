# Generated by Django 5.1.1 on 2024-10-23 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authUser', '0003_remove_user_email_user_name_alter_user_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='phone_number',
            new_name='username',
        ),
    ]