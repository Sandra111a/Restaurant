# Generated by Django 5.0.4 on 2024-04-25 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='password',
            new_name='password1',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='login',
            new_name='username',
        ),
    ]
