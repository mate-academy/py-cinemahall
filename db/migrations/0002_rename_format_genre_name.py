# Generated by Django 4.0.2 on 2024-08-21 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='format',
            new_name='name',
        ),
    ]
