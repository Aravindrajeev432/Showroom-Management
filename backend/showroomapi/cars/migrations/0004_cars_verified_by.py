# Generated by Django 4.1.4 on 2022-12-19 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_cars_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='verified_by',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
