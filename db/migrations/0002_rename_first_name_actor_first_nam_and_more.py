# Generated by Django 4.0.2 on 2023-03-08 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='first_name',
            new_name='first_nam',
        ),
        migrations.RenameField(
            model_name='actor',
            old_name='last_name',
            new_name='last_nam',
        ),
    ]
