# Generated by Django 4.0.2 on 2024-05-14 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='char',
            new_name='name',
        ),
    ]
