# Generated by Django 4.1.4 on 2023-01-23 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_baycurrentjob_baydetails_delete_bay'),
    ]

    operations = [
        migrations.AddField(
            model_name='baycurrentjob',
            name='bay',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bay', to='services.baydetails'),
        ),
        migrations.AddField(
            model_name='baydetails',
            name='status',
            field=models.CharField(choices=[('busy', 'busy'), ('free', 'free')], default='free', max_length=100),
            preserve_default=False,
        ),
    ]
