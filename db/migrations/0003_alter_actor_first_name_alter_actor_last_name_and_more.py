# Generated by Django 4.0.2 on 2025-01-06 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_rename_first_mame_actor_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='first_name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='actor',
            name='last_name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]
