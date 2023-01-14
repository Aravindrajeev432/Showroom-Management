# Generated by Django 4.1.4 on 2022-12-31 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_colours'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='displaycars',
            name='colour',
        ),
        migrations.AddField(
            model_name='displaycars',
            name='colour',
            field=models.ManyToManyField(to='cars.colours'),
        ),
    ]
