# Generated by Django 4.1.4 on 2023-01-14 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0022_alter_displaycarimages_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='universal_car_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cars',
            name='universal_part_number',
            field=models.CharField(max_length=100, null=True),
        ),
    ]