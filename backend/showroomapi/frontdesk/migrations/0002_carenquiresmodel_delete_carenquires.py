# Generated by Django 4.1.4 on 2023-01-11 04:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0016_displaycars_type'),
        ('frontdesk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarEnquiresmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_phone', models.CharField(max_length=20, null=True, validators=[django.core.validators.RegexValidator(message='Phone number should be 10 digits', regex='^\\d{10}$')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('completed', 'completed')], max_length=100, null=True)),
                ('display_car', models.ForeignKey(on_delete=django.db.models.deletion.SET, to='cars.displaycars')),
            ],
        ),
        migrations.DeleteModel(
            name='CarEnquires',
        ),
    ]
