# Generated by Django 4.0.2 on 2023-09-25 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_delete_actor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
            ],
        ),
    ]
