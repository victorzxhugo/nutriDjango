# Generated by Django 5.0.6 on 2024-06-17 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nutriApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicaoantropometrica',
            old_name='user_id',
            new_name='user',
        ),
    ]