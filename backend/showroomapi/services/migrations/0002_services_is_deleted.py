# Generated by Django 4.1.4 on 2022-12-29 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
